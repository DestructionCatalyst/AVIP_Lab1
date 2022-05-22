# Лабораторная работа №7. Текстурный анализ и контрастирование

- Параметры матрицы Харалика: d=1, phi = {45, 135, 225, 315}

- Расчет корелляции

- Кусочно-линейное контрастирование

- Повторное назожение матрицы Харалика и вычисление корелляции 
для контарстированного изображения

## Изображение 1. Ковер

### Исходное изображение

![Carpet](./img/src/carpet-texture.png)

### Полутоновое изображение

![Carpet](./img/out/semitone/carpet-texture.png)

### Матрица Харалика

![Carpet](./img/out/haralik/carpet-texture.png)

### Корелляция: -5.11850115574678e-25

### Гистограммы

![Carpet](./img/out/histograms/carpet-texture.png)

### Преобразованное изображение

![Carpet](./img/out/transformed/carpet-texture.png)

### Матрица Харалика для преобразованного изображения

![Carpet](./img/out/haralik_transformed/carpet-texture.png)

### Корелляция: -5.504346340411345e-25

## Изображение 2. Ткань

### Исходное изображение

![Cloth](./img/src/cloth-texture.png)

### Полутоновое изображение

![Cloth](./img/out/semitone/cloth-texture.png)

### Матрица Харалика

![Cloth](./img/out/haralik/cloth-texture.png)

### Корелляция: -1.6126538550883197e-31

### Гистограммы

![Cloth](./img/out/histograms/cloth-texture.png)

### Преобразованное изображение

![Cloth](./img/out/transformed/cloth-texture.png)

### Матрица Харалика для преобразованного изображения

![Cloth](./img/out/haralik_transformed/cloth-texture.png)

### Корелляция: -8.778472817170237e-30

## Изображение 3. Доски 

### Исходное изображение

![Wood](./img/src/wood-texture.png)

### Полутоновое изображение

![Wood](./img/out/semitone/wood-texture.png)

### Матрица Харалика

![Wood](./img/out/haralik/wood-texture.png)

### Корелляция: -5.127885449510635e-25

### Гистограммы

![Wood](./img/out/histograms/wood-texture.png)

### Преобразованное изображение

![Wood](./img/out/transformed/wood-texture.png)

### Матрица Харалика для преобразованного изображения

![Wood](./img/out/haralik_transformed/wood-texture.png)

### Корелляция: -1.8777786309721848e-23

## Выводы. 

Кусочно-линейное контрастирование обынчно делает изображение 
более распознаваемым с точки зрения человека, а с точки зрения
текстурного анализа оно делает матрицу Харалика более светлой и
как правило увеличивает ее корелляцию.