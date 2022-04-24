from PIL import Image
import numpy as np
from os import path

from resampling import interpolate, decimate, two_iteration_discretization, one_iteration_discretization
from semi_tone import to_semi_tone
from binarization import niblack_binarization


def prompt(variants: dict):
    for number, variant in enumerate(variants.keys(), 1):
        print(f'{number} - {variant}')
    input_correct = False
    user_input = 0
    while not input_correct:
        try:
            user_input = int(input('> '))
            if user_input <= 0 or user_input > len(variants):
                raise ValueError
            input_correct = True
        except ValueError:
            print("Введите корректное значение")
    return dict(enumerate(variants.values(), 1))[user_input]


def safe_number_input(number_type: type, lower_bound=None, upper_bound=None):
    input_correct = False
    user_input = 0
    while not input_correct:
        try:
            user_input = number_type(input('> '))
            if lower_bound is not None and user_input < lower_bound:
                raise ValueError
            if upper_bound is not None and user_input > upper_bound:
                raise ValueError
            input_correct = True
        except ValueError:
            print("Введите корректное значение")
    return user_input


images = {
    'Цифровой рисунок': 'digital_drawing.jpeg',
    'Картина': 'handmade_drawing.jpg',
    'Фото цветов': 'flowers_small.bmp',
    'Городской пейзаж': 'railway_station_small.bmp',
    'Рукописный текст': 'written_text_small.bmp',
    'Печатный текст': 'printed_text_small.bmp',
    'Старая книга': 'old_book.webp',
    'Старославянский текст': 'slavic_text.png'
}

operation_classes = {
    'Передискретизация': {
        'Интерполяция': interpolate,
        'Децимация': decimate,
        'Двухпроходная передискретизация': two_iteration_discretization,
        'Однопроходная передискретизация': one_iteration_discretization
    },
    'Обесцвечивание': to_semi_tone,
    'Бинаризация Ниблэка': niblack_binarization
}


if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = Image.open(path.join('img', 'src', selected_image)).convert('RGB')
    print('Выберите вид обработки:')
    selected_operation_class = prompt(operation_classes)
    args = []
    color_model = 'RGB'
    data_type = np.uint8
    if isinstance(selected_operation_class, dict):
        print('Выберите операцию:')
        selected_operation = prompt(selected_operation_class)
        if selected_operation == interpolate:
            print('Введите целый коэффициент растяжения')
            factor = safe_number_input(int, 1)
            args = [factor]
        if selected_operation == decimate:
            print('Введите целый коэффициент сжатия')
            factor = safe_number_input(int, 1)
            args = [factor]
        if selected_operation == two_iteration_discretization:
            print('Введите целый коэффициент растяжения')
            numerator = safe_number_input(int, 1)
            print('Введите целый коэффициент сжатия')
            denominator = safe_number_input(int, 1)
            args = [numerator, denominator]
        if selected_operation == one_iteration_discretization:
            print('Введите дробный коэффициент растяжения/сжатия')
            factor = safe_number_input(float, 0)
            args = [factor]
    elif callable(selected_operation_class):
        selected_operation = selected_operation_class
        color_model = 'L'
        if selected_operation == niblack_binarization:
            color_model = 'L'
    img.show()
    result = Image.fromarray(selected_operation(np.array(img), *args).astype(data_type), color_model)
    if selected_operation == niblack_binarization:
        result = result.convert("1")
    result.show()
    print('Введите название сохраненного изображения (оставьте пустым, чтобы не сохранять)')
    selected_path = input()
    if selected_path:
        result.save(path.join('img', 'out', selected_path))

