#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Dados(object):
    def __init__(self, rolagem='rolagem'):
        self.name = ('{}{}'.format(rolagem, random.randint(1, 100)))
        
    def rolagem(self, faces, quantidade, bonus=0, dificuldade=0):
        self.faces = faces
        self.quantidade = quantidade
        self.bonus = bonus
        self.dificuldade = dificuldade
        cont = 0
        d = []
        while cont < self.quantidade:
            d.append(random.randint(1, self.faces))
            cont += 1
        if self.dificuldade == 0:
            return(sum(d) + self.bonus)
        else:
            for n in d:
                if n >= self.dificuldade:
                    d.append(0)
                else:
                    pass
            return(d.count(0))

if __name__ == '__main__':
    main()
