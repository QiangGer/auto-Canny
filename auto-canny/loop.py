# -*- coding: UTF-8 -*-
import numpy as np
import copy


def loop(gradient):
    Max = np.max(gradient)
    Min = np.min(gradient)

    # T是初始平均值，Tnew是迭代平均值
    t = (Max + Min) / 2

    while True:
        imagemax = copy.deepcopy(gradient)
        imagemin = copy.deepcopy(gradient)
        imagemax[imagemax < t] = 0
        imagemin[imagemin >= t] = 0

        tnew = ((sum(imagemax[imagemax > 0]) / len(imagemax[imagemax > 0])) + sum(imagemin[imagemin > 0]) / len(
            imagemin[imagemin > 0])) / 2
        if abs(tnew - t) < 1:
            break
        else:
            t = tnew
    return tnew
