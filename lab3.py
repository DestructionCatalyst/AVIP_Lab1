from lab1 import prompt
from contoir import roberts
import numpy as np
from PIL import Image
from os import path
from difference import difference_image


images = {
    'Цифровой рисунок': 'digital_drawing_greyscale.bmp',
    'Печатный текст': 'printed_text_greyscale.bmp',
    'Рукописный текст': 'written_text_greyscale.bmp',
    'Картина': 'handmade_drawing_greyscale.bmp',
    'Старославянский текст': 'slavic_text_greyscale.bmp',
    'Фото цветов': 'flowers_greyscale.bmp',
    'Городской пейзаж': 'railway_station_greyscale.bmp',
}

operation_classes = {
    'Оператор Робертса': roberts,
}

operations = {
    'Градиентная матрица Gx': 'x',
    'Градиентная матрица Gy': 'y',
    'Градиентная матрица G': 'g',
    'Бинаризованная градиентная матрица G': 'b',
}

if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = Image.open(path.join('img', 'greyscale', selected_image)).convert('L')
    selected_operation_class = roberts
    print('Выберите вид обработки:')
    args = [prompt(operations), 64]
    folder = 'contoirs'
    img.show()
    result = Image.fromarray(selected_operation_class(np.array(img), *args).astype(np.uint8), "L")
    result.show()
    print('Введите название сохраненного изображения (оставьте пустым, чтобы не сохранять)')
    selected_path = input()
    if selected_path:
        result.save(path.join('img', folder, selected_path))
    # images = [
    #     'digital_drawing',
    #     'printed_text',
    #     'written_text',
    #     'handmade_drawing',
    #     'slavic_text',
    #     'flowers',
    #     'railway_station'
    # ]
    # methods = ['x', 'y', 'g', 'b']
    # for image in images:
    #     img = Image.open(path.join('img', 'greyscale', image + "_greyscale.bmp")).convert('L')
    #     img_arr = np.array(img)
    #     for method in methods:
    #         result = Image.fromarray(roberts(img_arr, direction=method).astype(np.uint8), "L")
    #         if method == 'b':
    #             result = result.convert("1")
    #         res_name = image + '_' + method + ".bmp"
    #         result.save(path.join('img', 'contoirs', res_name))
    #         print(res_name)
