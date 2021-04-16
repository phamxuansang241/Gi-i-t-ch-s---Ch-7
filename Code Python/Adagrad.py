import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x**2 + x + 9 * np.sin(x)


def d_func(x):
    h = 1e-7
    return ((func(x + h) - func(x - h)) / (2 * h))


def myGD(alpha, x0):
    x = [x0]
    ep = 1e-3

    sum_gradient_sq = d_func(x0) * d_func(x0)

    for it in range(1000):
        cur_alpha = alpha / (math.sqrt(sum_gradient_sq) + 1)
        x_new = x[-1] - cur_alpha * d_func(x[-1])
        sum_gradient_sq = sum_gradient_sq + d_func(x_new) * d_func(x_new)
        if abs(d_func(x_new)) < ep:
            break
        x.append(x_new)
    print("Số bước lặp: {}".format(it))
    print("Giá trị nhỏ nhất là {} với x = {}".format(x[-1], func(x[-1])))
    return (x[-1], func(x[-1]))


myGD(1, 2)
