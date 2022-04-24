from lab1 import prompt
from opening import img_open
import numpy as np
from PIL import Image
from os import path
from difference import difference_image


images = {
    'Печатный текст': 'printed_text_binarized.bmp',
    'Рукописный текст (мало деталей)': 'written_text_binarized_low_details.bmp',
    'Рукописный текст': 'written_text_binarized_zero_k.bmp',
    'Рукописный текст (много деталей)': 'written_text_binarized_positive_k.bmp',
    'Цифровой рисунок': 'digital_drawing_binarized.bmp',
    'Старославянский текст': 'slavic_text_binarized.bmp',
    'Фото цветов': 'flowers_binarized.bmp',
    'Городской пейзаж': 'railway_station_binarized.bmp',
}

images1 = {
    'Печатный текст': 'printed_text_opened.bmp',
    'Рукописный текст (мало деталей)': 'written_text_opened_low_details.bmp',
    'Рукописный текст': 'written_text_opened.bmp',
    'Рукописный текст (много деталей)': 'written_text_opened_high_details.bmp',
    'Фото цветов': 'flowers_opened.bmp',
    'Городской пейзаж': 'railway_station_opened.bmp',
}

operation_classes = {
    'Открытие': img_open,
    'Разностное изображение': difference_image
}

if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = Image.open(path.join('img', 'binarized', selected_image)).convert('L')
    print('Выберите вид обработки:')
    selected_operation_class = prompt(operation_classes)
    args = []
    folder = 'opened'
    if selected_operation_class == difference_image:
        print('Выберите второе изображение:')
        selected_image = prompt(images1)
        img1 = Image.open(path.join('img', 'opened', selected_image)).convert('L')
        args.append(img1)
        folder = 'difference_images'
        img1.show()
    img.show()
    result = Image.fromarray(selected_operation_class(np.array(img), *args).astype(np.uint8), "L").convert("1")
    result.show()
    print('Введите название сохраненного изображения (оставьте пустым, чтобы не сохранять)')
    selected_path = input()
    if selected_path:
        result.save(path.join('img', folder, selected_path))
