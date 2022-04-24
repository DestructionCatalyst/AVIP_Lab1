# (11 - 1) % 16 + 1 = 11
# d=1, phi = {45, 135, 225, 315} CORR Кусочно-линейное
from lab1 import prompt
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from os import path
from semi_tone import to_semi_tone
from haraliks_matrix import haraliks_matrix, corr
from contrast import piecewise_linear

images = {
    'Текстура дерева': 'wood-texture.png',
    'Текстура ткани': 'cloth-texture.png',
    'Текстура ковра': 'carpet-texture.png',
}

if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = Image.open(path.join('img', 'src', selected_image))
    img_arr = np.array(img)

    semitone = to_semi_tone(img_arr)
    semitone_img = Image.fromarray(semitone.astype(np.uint8), "L")
    semitone_img.save(path.join('img', 'out', 'semitone', selected_image))
    semitone_img.show()

    transformed = piecewise_linear(semitone)
    transformed_img = Image.fromarray(transformed.astype(np.uint8), "L")
    transformed_img.save(path.join('img', 'out', 'transformed', selected_image))
    transformed_img.show()

    figure, axis = plt.subplots(2, 1)
    axis[0].hist(x=semitone.flatten(), bins=np.arange(0, 255))
    axis[1].hist(x=transformed.flatten(), bins=np.arange(0, 255))
    plt.savefig(path.join('img', 'out', 'histograms', selected_image))
    # plt.show()

    matrix = haraliks_matrix(semitone.astype(np.uint8))
    result = Image.fromarray(matrix.astype(np.uint8), "L")
    result.save(path.join('img', 'out', 'haralik', selected_image))
    result.show()

    t_matrix = haraliks_matrix(transformed.astype(np.uint8))
    t_result = Image.fromarray(t_matrix.astype(np.uint8), "L")
    t_result.save(path.join('img', 'out', 'haralik_transformed', selected_image))
    t_result.show()

    print(f"Correlation: {corr(matrix)}")
    print(f"Correlation (transformed): {corr(t_matrix)}")
