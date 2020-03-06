#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:14:49 2020

@author: claudeedirecto
"""

"""
File: die.py

"""

from random import randint

class Die:

    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = randint(1, 6)

    def getValue(self):
        return self.value

    def __str__(self):
        return str(self.getValue())
    
