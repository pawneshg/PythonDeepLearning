# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:21:07 2018

@author: admin
"""
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    tempLeft = [0]*(n1)
    tempRight = [0]*(n2)
    
    for i in range(0, n1):
        tempLeft[i] = arr[left + i]

    for i in range(0, n2):
        tempRight[i] = arr[mid + 1 + i]
    
    i = 0 #Intial index for first sub array
    j = 0 #Intial index for seconf subarray
    k = 1 #Initial index for merged subarray
    
    while i < n1 and j < n2:
        if tempLeft[n1] <= tempRight[j]:
            arr[k] = tempLeft[i]
            i+=1
        else:
            arr[k] = tempRight[j]
            j+=1
        k+=1
    
    #cpy the remaining ele of tempLeft if der r any
    while i < n1:
        arr[k] = tempLeft[i]
        i+=1
        k+=1
    while j < n2:
        arr[k] = tempRight[j]
        j +=1
        k +=1
        

def mergeSort(arr, left, right):
    mid = (left+(right-1))/2
    
    mergeSort(arr, left, mid)
    mergeSort(arr, mid+1, right)
    merge(arr, left, mid, right)

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)

mergeSort(arr, 0, n-1)
print "sorted array :\n"

for i in arr:
    print i
