# Лабораторная работа №3. Выделение контуров на изображении

Реализовано: - Выделение контуров оператором Робертса 3х3 
с формулой градиента   
<img src="https://latex.codecogs.com/svg.latex?\Large&space;G=\sqrt{G_x^2+G_y^2}" title="G=\sqrt{G_x^2+G_y^2}" />

Для каждого градиентного изображения проводится 
статическая бинаризация. Порог бинаризации - 32, 
если не указано иное

## Результаты

### Изображение 1. Мультипликационное изображение

![Marisad](./img/digital_drawing_greyscale.bmp)\
Исходное изображение

![Marisad](./img/digital_drawing_x.bmp)\
Градиент по X

![Marisad](./img/digital_drawing_y.bmp)\
Градиент по Y

![Marisad](./img/digital_drawing_g.bmp)\
Общая градиентная матрица

![Marisad](./img/digital_drawing_b.bmp)\
Бинаризованная градиентная матрица

### Изображение 2. Печатный текст

![Printed text](./img/printed_text_greyscale.bmp)\
Исходное изображение

![Printed text](./img/printed_text_x.bmp)\
Градиент по X

![Printed text](./img/printed_text_y.bmp)\
Градиент по Y

![Printed text](./img/printed_text_g.bmp)\
Общая градиентная матрица

![Printed text](./img/printed_text_b.bmp)\
Бинаризованная градиентная матрица

### Изображение 3. Цветы

![Flowers](./img/flowers_greyscale.bmp)\
Исходное изображение

![Flowers](./img/flowers_x.bmp)\
Градиент по X

![Flowers](./img/flowers_y.bmp)\
Градиент по Y

![Flowers](./img/flowers_g.bmp)\
Общая градиентная матрица

![Flowers](./img/flowers_b.bmp)\
Бинаризованная градиентная матрица

### Изображение 4. Мона Лиза

![Mona Lisa](./img/handmade_drawing_greyscale.bmp)\
Исходное изображение

![Mona Lisa](./img/handmade_drawing_x.bmp)\
Градиент по X

![Mona Lisa](./img/handmade_drawing_y.bmp)\
Градиент по Y

![Mona Lisa](./img/handmade_drawing_g.bmp)\
Общая градиентная матрица

![Mona Lisa](./img/handmade_drawing_b.bmp)\
Бинаризованная градиентная матрица (порог 32)
 
![Mona Lisa](./img/handmade_drawing_b_16.bmp)\
Бинаризованная градиентная матрица (порог 16)

## Выводы

Выделение контуров с помощью оператора Робертса 
хорошо себя показыват на изображениях с четкими линиями, 
например мультипликационных ихображениях. Также метод
хорошо справляется с выделением контуров объектов на фотографиях,
сделанных крупным планом, но в случае большого количества деталей 
они могут быть трудно различимы.

Для изображений текста и картин результаты немного хуже, 
но при грамотном пороге бинаризации в большинстве случаев
можно получить удоволетворительный результат
