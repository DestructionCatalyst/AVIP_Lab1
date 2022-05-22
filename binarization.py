# (11 - 1) % 8 + 1 = 3
import numpy as np
from semi_tone import to_semi_tone
from util import limit, area_of_frame


def integral_images(img: np.array) -> np.array:
    integral_img = np.empty_like(img)
    integral_square_img = np.empty_like(img)
    integral_img[0, 0] = img[0, 0]
    integral_square_img[0, 0] = img[0, 0] ** 2
    for x in range(1, img.shape[0]):
        integral_img[x, 0] = img[x, 0] + integral_img[x - 1, 0]
        integral_square_img[x, 0] = img[x, 0] ** 2 + integral_square_img[x - 1, 0]
    for y in range(1, img.shape[1]):
        integral_img[0, y] = img[0, y] + integral_img[0, y - 1]
        integral_square_img[0, y] = img[0, y] ** 2 + integral_square_img[0, y - 1]
    for x in range(1, img.shape[0]):
        for y in range(1, img.shape[1]):
            integral_img[x, y] = img[x, y] - integral_img[x - 1, y - 1] \
                                 + integral_img[x - 1, y] + integral_img[x, y - 1]
            integral_square_img[x, y] = img[x, y] ** 2 - integral_square_img[x - 1, y - 1] \
                                        + integral_square_img[x - 1, y] + integral_square_img[x, y - 1]
    return integral_img, integral_square_img


def sum_in_frame(integral_img: np.array, x: int, y: int, frame_size: int):
    return (integral_img[limit(x + frame_size // 2, 0, integral_img.shape[0] - 1),
                         limit(y + frame_size // 2, 0, integral_img.shape[1] - 1)] -
            integral_img[limit(x + frame_size // 2, 0, integral_img.shape[0] - 1),
                         limit(y - frame_size // 2, 0, integral_img.shape[1] - 1)] -
            integral_img[limit(x - frame_size // 2, 0, integral_img.shape[0] - 1),
                         limit(y + frame_size // 2, 0, integral_img.shape[1] - 1)] +
            integral_img[limit(x - frame_size // 2, 0, integral_img.shape[0] - 1),
                         limit(y - frame_size // 2, 0, integral_img.shape[1] - 1)])


def niblack_binarization(img: np.array, frame_size: int = 15, k: float = 0.2) -> np.array:
    if len(img.shape) == 3 and img.shape[2] == 3:
        img = to_semi_tone(img)
    integral_img, integral_square_img = integral_images(img)
    m = np.empty_like(img)
    d = np.empty_like(img)
    t = np.empty_like(img)
    res_img = np.empty_like(img)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            m[x, y] = (sum_in_frame(integral_img, x, y, frame_size) //
                       area_of_frame(x, y, frame_size, img.shape[0], img.shape[1]))
            d[x, y] = (sum_in_frame(integral_square_img, x, y, frame_size) //
                       area_of_frame(x, y, frame_size, img.shape[0], img.shape[1]) - m[x, y] ** 2)
            t[x, y] = m[x, y] + k * np.sqrt(d[x, y])
            res_img[x, y] = 0 if img[x, y] < t[x, y] else 255
    return res_img


def static_binarization(img, border):
    if len(img.shape) == 3 and img.shape[2] == 3:
        img = to_semi_tone(img)
    return np.fromiter(map(
                lambda pixel: 255 if pixel > border else 0,
                img.flatten()
            ), dtype=np.uint8).reshape(img.shape)
