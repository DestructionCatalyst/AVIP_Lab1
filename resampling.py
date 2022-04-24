import numpy as np


def interpolate(img: np.array, factor: int) -> np.array:
    dimensions = img.shape[0:2]
    new_dimensions = tuple(dimension * factor for dimension in dimensions)
    new_shape = (*new_dimensions, img.shape[2])
    new_img = np.empty(new_shape)
    for x in range(new_dimensions[0]):
        for y in range(new_dimensions[1]):
            new_img[x, y] = img[
                min(int(round(x / factor)), dimensions[0] - 1),
                min(int(round(y / factor)), dimensions[1] - 1)
            ]
    return new_img


def decimate(img: np.array, factor: int) -> np.array:
    dimensions = img.shape[0:2]
    new_dimensions = tuple(int(round(dimension / factor)) for dimension in dimensions)
    new_shape = (*new_dimensions, img.shape[2])
    new_img = np.empty(new_shape)
    for x in range(new_dimensions[0]):
        for y in range(new_dimensions[1]):
            new_img[x, y] = img[
                min(x * factor, dimensions[0] - 1),
                min(y * factor, dimensions[1] - 1)
            ]
    return new_img


def two_iteration_discretization(img: np.array, numerator: int, denominator: int) -> np.array:
    return decimate(interpolate(img, numerator), denominator)


def one_iteration_discretization(img: np.array, factor: float) -> np.array:
    dimensions = img.shape[0:2]
    new_dimensions = tuple(int(round(dimension * factor)) for dimension in dimensions)
    new_shape = (*new_dimensions, img.shape[2])
    new_img = np.empty(new_shape)
    for x in range(new_dimensions[0]):
        for y in range(new_dimensions[1]):
            new_img[x, y] = img[
                min(int(round(x / factor)), dimensions[0] - 1),
                min(int(round(y / factor)), dimensions[1] - 1)
            ]
    return new_img

