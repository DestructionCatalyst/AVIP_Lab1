import numpy as np
from util import limit


def piecewise_linear(img: np.array):
    flat_img = img.flatten()
    start, end = np.quantile(flat_img, 0.01), np.quantile(flat_img, 0.99)
    transform = lambda x: limit((x - start) * int(255 / (end - start)), 0, 255)
    return np.vectorize(transform)(img)
