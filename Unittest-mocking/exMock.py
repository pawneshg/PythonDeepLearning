# -*- coding: utf-8 -*-
"""
Created on Mon May 21 18:28:07 2018

@author: admin
"""

class ProductionClass:
    
    def user_api(self, a, b = False):
        if b:
            return self._internal_api_one(a)
        else:
            return self._internal_api_two(a)
    
    def _internal_api_one(self, a):
        pass
    
    def _internal_api_two(self, a):
        pass
    