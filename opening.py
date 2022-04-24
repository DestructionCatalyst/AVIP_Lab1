# (11 - 1) % 12 + 1 = 11
import numpy as np
from util import limit


def img_open(img: np.array, frame_size: int = 3) -> np.array:
    new_img = np.empty_like(img)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            frame = img[
                    limit(x - frame_size // 2, 0, img.shape[0] - 1):limit(x + frame_size // 2 + 1, 0, img.shape[0] - 1),
                    limit(y - frame_size // 2, 0, img.shape[1] - 1):limit(y + frame_size // 2 + 1, 0, img.shape[1] - 1)
                ]
            new_img[x, y] = 255 if np.min(frame) == 255 else 0
    return new_img
