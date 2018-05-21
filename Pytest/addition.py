# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:37:17 2018

@author: admin
"""

def add(a, b):
    if a > 0 and b > 0:
        return a+b
    else:
        return None

def add_with_exception(a, b):
    if a> 0 and b > 0:
        return a+b
    else:
        raise ValueError