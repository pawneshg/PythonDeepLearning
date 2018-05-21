# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:34:55 2018

@author: admin
"""

from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()
    
with open_file('sampleFile.txt') as f:
    f.write('sample file creation using generator context manager')
