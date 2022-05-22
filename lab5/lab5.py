from binarization import niblack_binarization
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from os import path

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
    letter_borders = []
    letter_start = 0
    is_empty = True
    for i in range(img.shape[1]):
        if profile[i] == 0:
            if not is_empty:
                is_empty = True
                letters.append(img[:, letter_start:i+1])
                letter_borders.append(i+1)
        else:
            if is_empty:
                is_empty = False
                letter_start = i
                letter_borders.append(letter_start)
    letters.append(img[:, letter_start:img.shape[1] - 1])
    print(letter_borders)
    return letters, letter_borders


def bar(data, bins, axis):
    if axis == 1:
        plt.bar(x=bins, height=data)
        # plt.ylim(0, 52)
    elif axis == 0:
        plt.barh(y=bins, width=data)
        # plt.ylim(52, 0)
    else:
        raise ValueError('Invalid axis')


if __name__ == '__main__':
    img = Image.open('img/src/sentence.png')

    img_arr = np.array(img)[:, :, :3]
    binarized_img_arr = 255 - niblack_binarization(img_arr)

    profile_x = calculate_profile(binarized_img_arr, 0)
    profile_y = calculate_profile(binarized_img_arr, 1)
    bins_x = np.arange(start=1, stop=img_arr.shape[0] + 1).astype(int)
    bins_y = np.arange(start=1, stop=img_arr.shape[1] + 1).astype(int)

    bar(profile_x / 255, bins_x, 0)
    plt.savefig(path.join('img', 'out', f'profile_x.png'))
    plt.clf()
    bar(profile_y / 255, bins_y, 1)
    plt.savefig(path.join('img', 'out', f'profile_y.png'))
    plt.clf()

    img_cut_x, profile_x = cut_white(binarized_img_arr, profile_x, 0)
    img_cut, profile_y = cut_white(img_cut_x, profile_y, 1)

    img_letters, letter_borders = split_letters(img_cut, profile_y)

    result_img = Image.fromarray(255 - img_cut.astype(np.uint8), 'L')
    result_img.save(f"img/out/cut.bmp")
    rgb_img = Image.new("RGB", result_img.size)
    rgb_img.paste(result_img)
    draw = ImageDraw.Draw(rgb_img)
    for border in letter_borders:
        draw.line((border, 0, border, img_cut.shape[1]), fill='red')
    rgb_img.show()
    rgb_img.save(f"img/out/result.bmp")

    for i, letter in enumerate(img_letters):
        letter_img = Image.fromarray(letter.astype(np.uint8), 'L').convert('1')
        letter_img.save(f"img/out/letter_{i}.bmp")
