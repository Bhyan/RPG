#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Dice(object):
    def __init__(self, scrolling='scrolling'):
        self.name = ('{}{}'.format(scrolling, random.randint(1, 100)))

    def scrolling(self, faces, quantity, bonus=0, difficulty=0):
        self.faces = faces
        self.quantity = quantity
        self.bonus = bonus
        self.difficulty = difficulty
        count = 0
        d = []
        while count < self.quantity:
            d.append(random.randint(1, self.faces))
            count += 1
        if self.difficulty == 0:
            return(sum(d) + self.bonus)
        else:
            for n in d:
                if n >= self.dificulty:
                    d.append(0)
                else:
                    pass
            return(d.count(0))

if __name__ == '__main__':
    main()
