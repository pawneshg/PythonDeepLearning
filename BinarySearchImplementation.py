# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:08:37 2018

@author: admin
"""

def binarySearch(arr, start, end, item):
    if end > 1:
        mid = start + (end - 1)/2
        if arr[mid] == item:
            return mid
        
        elif arr[mid] > item:
            return binarySearch(arr, start, mid-1, item)
        else:
            return binarySearch(arr, mid+1, end, item)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
arr = sorted(arr)
item = 10

result = binarySearch(arr, 0, len(arr)-1, item)

print result