import numpy as np


def to_semi_tone(img: np.array) -> np.array:
    return img.sum(axis=2) / 3
