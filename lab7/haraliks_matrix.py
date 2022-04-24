import numpy as np


def haraliks_matrix(img_arr: np.array, d=1):
    matrix = np.zeros(shape=(256, 256))

    for x in range(d, img_arr.shape[0] - d):
        for y in range(d, img_arr.shape[1] - d):
            matrix[img_arr[x-d, y-d], img_arr[x, y]] += 1
            matrix[img_arr[x+d, y+d], img_arr[x, y]] += 1
            matrix[img_arr[x+d, y-d], img_arr[x, y]] += 1
            matrix[img_arr[x-d, y+d], img_arr[x, y]] += 1

    return matrix


def mean(matr: np.array):
    sum = 0
    for i in range(matr.shape[0]):
        sum += i * matr.sum(axis=1)[i]
    return sum


def var(matr: np.array, axis, mu=None):
    if mu is None:
        mu = mean(matr)
    sum = 0
    for i in range(matr.shape[1 - axis]):
        sum += (i - mu) ** 2 * matr.sum(axis=axis)[i]
    return sum


def corr(matr: np.array):
    sum = 0
    for i in range(matr.shape[0]):
        for j in range(matr.shape[1]):
            sum += i * j * matr[i, j]
    mu = mean(matr)
    var_x, var_y = var(matr, 0, mu), var(matr, 1, mu)
    print(f"mu={mu}, var_x={var_x}, var_y={var_y}")
    return (sum - mu ** 2) / (var_x * var_y)
