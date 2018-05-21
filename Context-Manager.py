# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:26:57 2018

@author: admin
"""

class File():
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file
    def __exit__(self, *args):
        self.open_file.close()

files = []

for _ in range(100):
    with File('sampleFile.txt', 'w') as fp:
        fp.write('sample file')
        files.append(fp)
print files