import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

    def func(x):
        return x**2 + x + 9 * np.sin(x)

    def d_func(x):
        h = 1e-7
        return ((func(x + h) - func(x - h)) / (2 * h))


def GD_momentum_NAG(x0, gamma, alpha):
    ep = 1e-3

    x = [x0]
    v_old = np.zeros_like(x0)

    for it in range(100000):
        v_new = gamma * v_old + alpha * d_func(x[-1] - gamma * v_old)
        x_new = x[-1] - v_new
        if (abs(d_func(x_new)) < ep):
            break
        x.append(x_new)
        v_old = v_new
    print("Số bước lặp: {}".format(it))
    print("Giá trị nhỏ nhất là {} với x = {}".format(x[-1], func(x[-1])))
    return (x[-1], func(x[-1]))


GD_momentum_NAG(5, 0.9, 0.1)
