#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import imp
dado = imp.load_source('dado', '../Dado/dado.py')


class TestDados(unittest.TestCase):
    def test_rolagem(self):
        obj = dado.Dados()
        obj.rolagem(4, 100)
        obj.rolagem(6, 100)
        obj.rolagem(10, 100)
        obj.rolagem(12, 100)
        obj.rolagem(20, 100)
        obj.rolagem(100, 100)

class DataTable(object):
    '''Teste de rolagem dos possíveis dados de RPG, com 100 lançamento de cada 
unidade do dado escolhido.
    '''

if __name__ == '__main__':
    unittest.main()
