# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:45:50 2018

@author: admin
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        
    def first(self):
        return self.items[0]
    
    def last(self):
        return self.items[-1]
    
    def length(self):
        return len(self.items)