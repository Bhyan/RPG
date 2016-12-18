#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import dice
# import imp
# dado = imp.load_source('dado', '../Dado/dado.py')


class Testdices(unittest.TestCase):
    def setUp(self):
        pass

    def test_scrolling(self):
        '''Rolling test of possible RPG dices, with 100 release of each unit of
        the chosen dice.'''
        obj = dice.Dice()
        obj.scrolling(4, 100)
        obj.scrolling(6, 100)
        obj.scrolling(10, 100)
        obj.scrolling(12, 100)
        obj.scrolling(20, 100)
        obj.scrolling(100, 100)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
