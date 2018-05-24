# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:13:34 2018

@author: admin
"""

#FuzzBizz
#https://www.hackerrank.com/challenges/fizzbuzz/problem
for i in range(101):
    print max(str(i), ''+(i%3==0)*'Fizz'+(i%5==0)*'Buzz')