import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import path
from PIL import Image
from lab4.generation import symbol_set, filename
from functools import cache
from itertools import product


class FeatureImage:
    def __init__(self, img: Image, invert=True):
        if invert:
            self.img = 1 - np.array(img)
        else:
            self.img = np.array(img)

    @property
    def shape(self):
        return self.img.shape

    def __getitem__(self, key):
        return self.img[key]

    @cache
    def line_by_line_moment(self, p: int, q: int) -> int:
        moment = 0
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                moment += x ** p * y ** q * self[x, y]
        return moment

    def weight(self) -> int:
        return self.line_by_line_moment(0, 0)

    def area(self) -> int:
        return self.shape[0] * self.shape[1]

    def relative_weight(self) -> float:
        return self.weight() / self.area()

    def center(self, axis: int) -> float:
        if axis not in (0, 1):
            raise ValueError("Invalid axis")
        # 1, 0 if axis == 0; 0, 1 if axis == 0
        p = int(not axis)
        q = axis
        return self.line_by_line_moment(p, q) / self.weight()

    def relative_center(self, axis: int) -> float:
        normalization_factor = self.shape[axis] - 1
        return (self.center(axis) - 1) / normalization_factor

    @cache
    def central_moment(self, p, q):
        x_bar = self.center(0)
        y_bar = self.center(1)
        moment = 0
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                moment += (x - x_bar) ** p * (y - y_bar) ** q * self[x, y]
        return moment

    def inertia(self, axis):
        if axis not in (0, 1):
            raise ValueError("Invalid axis")
        # 0, 2 if axis == 0; 2, 0 if axis == 0
        p = axis * 2
        q = (1 - axis) * 2
        return self.central_moment(p, q)

    def relative_inertia(self, axis):
        return self.inertia(axis) / self.weight() ** 2

    def profile(self, axis):
        return np.sum(self.img, axis=1 - axis), np.arange(start=1, stop=self.shape[axis] + 1).astype(int)

    def profile_norm(self, axis):
        return np.sum(self.img, axis=1 - axis) / self.shape[1 - axis]


def bar(data, bins, axis):
    if axis == 1:
        plt.bar(x=bins, height=data)
        plt.ylim(0, 52)
    elif axis == 0:
        plt.barh(y=bins, width=data)
        plt.ylim(52, 0)
    else:
        raise ValueError('Invalid axis')


def axis_name(axis):
    # x if axis == 0, y if axis == 1
    return 'x' * (1 - axis) + 'y' * axis


def join_names(*args):
    return '_'.join(filter(lambda string: string != '', args))


if __name__ == '__main__':
    # Calculate features
    df = pd.DataFrame()
    feature_images = {letter: FeatureImage(Image.open(filename(i))) for i, letter in enumerate(symbol_set)}
    df['letter'] = feature_images.keys()
    non_directed_features = ['weight']
    features = ['center', 'inertia']
    relativities = ['', 'relative']
    directions = [0, 1]
    for feature, relativity in product(non_directed_features, relativities):
        name = join_names(relativity, feature)
        df[name] = list(map(lambda img: getattr(img, name)(), feature_images.values()))
    for feature, relativity, axis in product(features, relativities, directions):
        name = join_names(relativity, feature)
        df[f'{name}_{axis_name(axis)}'] = list(map(lambda img: getattr(img, name)(axis), feature_images.values()))
    df.to_csv('features.csv', index=False)
    # Draw profiles
    for i, img in enumerate(feature_images.values()):
        for axis in (0, 1):
            profile, bins = img.profile(axis)
            # x if axis == 0, y if axis == 1
            folder = axis_name(axis)
            bar(profile, bins, axis)
            plt.savefig(path.join('profiles', folder, f'{str(i + 1).zfill(2)}'))
            plt.clf()
