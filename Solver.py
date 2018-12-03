#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


class Solver(object):
    # import math
    @staticmethod
    def calculate123():
        a111 = int(input('a: '))
        cdr = int(input('b: '))
        cca1 = int(input('cca1: '))
        d = cdr ** 2 - 4 * a111 * cca1

        if d >= 0:
            disc = math.sqrt(d)
            root3 = (-cdr + disc) / (2 * a111)
            root2 = (-cdr - disc) / (2 * a111)
            print(root3, root2)
        else:
            print('error')


Solver().calculate123()  # 注释
Solver.calculate123()



