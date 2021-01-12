#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 20:35:29 2021

@author: kaydee
"""

class RandomPit():
    def __init__(self,seed,isInt=True):
        self.seed = seed
        
        self.method = self.set_method(isInt)
        self.pro_seed = lambda x: (x*2)*self.method(x**2)
        
        self.iterator = 0
        
    def set_method(self,isInt):
        if isInt:
            return int 
        return float
        
    def random(self):
        self.iterator+=1
        return self.method(self.pro_seed(self.iterator)%self.seed**0.5)
        
        
randgen = RandomPit(seed = 555, isInt = True)

for i in range(100):
    print(randgen.random())
            