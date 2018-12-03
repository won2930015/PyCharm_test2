#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


class Solver(object):
    # import math
    def calculate123(self):

        a = int(input('a:'))
        b = int(input('b:'))
        c = int(input('c:'))
        d = b ** 2 - 4 * a * c
        if d >= 0:
            disc = math.sqrt(d)
            root3 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            print(root3, root2)
        else:
            print('error')

    def aaa(self):
        pass




Solver().calculate123()  # 注释
# Solver.calculate123()



