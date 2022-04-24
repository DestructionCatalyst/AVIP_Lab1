from binarization import niblack_binarization
import numpy as np
from PIL import Image


def calculate_profile(img: np.array, axis: int) -> np.array:
    return np.sum(img, axis=1 - axis)


def cut_white(img: np.array, profile: np.array, axis: int) -> np.array:
    start = profile.nonzero()[0][0]
    end = profile.nonzero()[0][-1] + 1
    # print(start, end, axis)
    if axis == 0:
        return img[start:end, :], profile[start:end]
    elif axis == 1:
        return img[:, start:end], profile[start:end]


# линии разреза
def split_letters(img: np.array, profile: np.array):
    assert img.shape[1] == profile.shape[0]
    letters = []
    letter_start = 0
    is_empty = True
    for i in range(img.shape[1]):
        if profile[i] == 0:
            if not is_empty:
                is_empty = True
                letters.append(img[:, letter_start:i+1])
        else:
            if is_empty:
                is_empty = False
                letter_start = i
    letters.append(img[:, letter_start:img.shape[1] - 1])
    return letters


if __name__ == '__main__':
    img = Image.open('img/src/sentence2.png')

    img_arr = np.array(img)[:, :, :3]
    binarized_img_arr = 255 - niblack_binarization(img_arr)

    profile_x = calculate_profile(binarized_img_arr, 0)
    profile_y = calculate_profile(binarized_img_arr, 1)

    img_cut_x, profile_x = cut_white(binarized_img_arr, profile_x, 0)
    img_cut, profile_y = cut_white(img_cut_x, profile_y, 1)

    img_letters = split_letters(img_cut, profile_y)

    Image.fromarray(img_cut.astype(np.uint8), 'L').convert('1').show()

    for i, letter in enumerate(img_letters):
        letter_img = Image.fromarray(letter.astype(np.uint8), 'L').convert('1')
        letter_img.save(f"img/out/letter_{i}.bmp")
