# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from Solver import Solver
_author_ = 'Administrator'
_project_ = 'PyCharm_test'



class TestSolver(TestCase):

    def test_negative_discr(self):
        s = Solver()
        self.assertRaises(Exception, s.demo, 2, 1, 2)

    def test_demo(self):
        self.fail()
