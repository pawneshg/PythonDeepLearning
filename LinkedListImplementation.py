# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:29:21 2018

@author: admin
"""
class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, n):
        self.next_node = n
        
class LinkedList(object):
    def __init__(self, r = None):
        self.root = r #//head
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size +=1
    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next_node(this_node.get_next_node())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next_node()
        return False
    
    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next_node()
        return None
    
myList = LinkedList()
myList.add(5)
myList.add(15)
myList.add(25)
print(myList)
print(myList.remove(15))
print(myList.find(25))

                
        
        
    
    
    
    
    
    
            
            
            
            
            
            
            
            
                    
        

