#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


class Solver(object):
    # <editor-fold desc="Description">
    def demo(self, a, b, c):

        # a = int(input('a:'))
        # b = int(input('b:'))
        # c = int(input('c:'))
        d = b ** 2 - 4 * a * c
        if d >= 0:
            disc=math.sqrt(d)
            root3 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            print(root3, root2)
        else:
            raise Exception
            # print('error')



Solver().demo(2, 1, 0)  # 注释
# # Solver.calculate123()



