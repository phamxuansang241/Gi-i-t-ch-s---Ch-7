import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

import_pnt = []
a = -5
b = 5
learning_rate = 0.1

def func(x):
    return x**2 + x + 9*np.sin(x)

def d_func(x):
    h = 1e-7
    return ((func(x + h) - func(x - h))/(2 * h))

def myGD(alpha, x0, sign):
    x = [x0]
    ep = 1e-3
    for it in range(1000):
        x_new = x[-1] + sign*alpha*d_func(x[-1])
        if abs(d_func(x_new)) < ep:
            break
        if (x[-1] > b):
            break
        x.append(x_new)

    if(x[-1] < b):
        print("Số bước lặp để tới điểm cực trị {} là: {}".format(x[-1], it))
    return (x[-1])

def get_local_maxmin(fi, se):
    x = fi
    step = 1e-2
    while(x < se):
        if(d_func(x) < 0):
            import_pnt.append(myGD(learning_rate, x, -1))
            x = import_pnt[-1] + step
        else:
            import_pnt.append(myGD(0.1, x, 1))
            x = import_pnt[-1] + step

    import_pnt.pop()

def solve():
    maximum = func(a)
    x_max = a
    minimum = func(a)
    x_min = a

    for it in import_pnt:
        if(func(it) > maximum):
            maximum = func(it)
            x_max = it
        if(func(it) < minimum):
            minimum = func(it)
            x_min = it


    if(func(b) < minimum):
        minimum = func(b)
        x_min = b
    if(func(b) > maximum):
        maximum = func(b)
        x_max = b

    print("Giá trị lớn là {} với x = {}".format(maximum, x_max))
    print("Giá trị nhỏ là {} với x = {}".format(minimum, x_min))

    return (x_min, minimum, x_max, maximum)


get_local_maxmin(a, b)
solve()

