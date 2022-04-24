# (11 - 1) % 10 + 1 = 1
import numpy as np
from typing import Literal
from binarization import static_binarization

operators = {
    'x': np.array(
        [[0, 0, 0],
         [0, -1, 0],
         [0, 0, 1]]
    ),
    'y': np.array(
        [[0, 0, 0],
         [0, 0, -1],
         [0, 1, 0]]
    )
}


def apply_operator(frame: np.array, direction: Literal['x', 'y', 'g', 'b']):
    frame = frame.astype(np.int32)
    if direction == 'x':
        return np.sum(operators['x'] * frame)
    elif direction == 'y':
        return np.sum(operators['y'] * frame)
    elif direction == 'g' or direction == 'b':
        return np.sqrt(np.sum(operators['x'] * frame) ** 2 + np.sum(operators['y'] * frame) ** 2)
    else:
        raise ValueError("Unsupported direction")


def get_frame(img: np.array, x: int, y: int) -> np.array:
    return img[x - 3 // 2:x + 3 // 2 + 1,
               y - 3 // 2:y + 3 // 2 + 1]


def roberts(img: np.array, direction: Literal['x', 'y', 'g', 'b'], binarization_border=32) -> np.array:
    new_img = np.zeros_like(img, dtype=np.float64)
    x, y = 1, 1
    while x < img.shape[0] - 1:
        if x % 2 == 0:
            while y + 1 < img.shape[1] - 1:
                frame = get_frame(img, x, y)
                new_img[x, y] = apply_operator(frame, direction)
                y += 1
        else:
            while y - 1 > 1:
                frame = get_frame(img, x, y)
                new_img[x, y] = apply_operator(frame, direction)
                y -= 1
        x += 1
    new_img = new_img / np.max(new_img) * 255
    if direction == 'b':
        return static_binarization(new_img, binarization_border)
    elif direction == 'x' or direction == 'y' or direction == 'g':
        return new_img.astype(np.uint8)
    else:
        raise ValueError("Unsupported direction")
