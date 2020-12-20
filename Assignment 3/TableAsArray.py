# -*- coding: utf-8 -*-

# Code is inspired by the class TableAsList, which is written by Lena Kallin Westin.
# Written by Rasmus Säfvenberg <rasmus.safvenberg@umu.se>.
# May be used in the course Datastrukturer och Algoritmer (Python) at Umeå University.
# Usage exept those listed above requires permission by the author.

# Version 2020-03-19.
# File has been updated 2020-03-19 to remove the usage of None in the functions. 
# The table now uses a counter variable instead to keep track of the amount of 
# elements in the table. The remove function has also been reworked and optimized.

from Array import Array

"""
The given class Table is an implementation of the datatype Table, which is 
constructed using the datatype Array. The interface of the class is given on
page 117 in  Lars-Erik Janlert, Torbjörn Wiberg; Datatyper och algoritmer 
2., [rev.] uppl.,Lund, Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7
"""
class Table:
       
    def __init__(self):
        """
            Purpose: Create a new instance of a Table, constructed as an array.
            Parameters: -
            Returns: -
            Comment: The size of the array can be altered by changing the 
                     lo and hi arguments.
                     Count gives the number of elements in the table.
        """
        self._table = Array(lo=(0,), hi=(2000,))
        self.count = 0
        
    def insert(self, key, obj):
        """
            Purpose: Insert a key, with a connected value, or overwrite the 
                     existing value connected to the given key in the table.
            Parameters: key - the name of the key connected to the object
                        obj - the value of the object to be inserted
            Returns: -
            Comment: If a Key with the same name as the argument key already
                     exists, the value of the existing object is overwritten and
                     the number of elements in the table remain the same.
                     When a new element is inserted, the count is 
                     increased by 1. 
                     If the table is full a new element will not be inserted.
        """
        if self.isempty():
            self._table.setValue(self._table.low(), (key,obj))
            self.count = self.count + 1     
            
        else:
            pos = self._table.low()[0]
            found = False
            while not found and pos < self.count:
                (newKey, newVal) = self._table.inspectValue((pos,))
                if newKey == key:
                    self._table.setValue((pos,), (key, obj))                    
                    found = True
                pos = pos + 1    
                
            if not found:
                if self.count < self._table.high()[0]:
                    self._table.setValue((pos,), (key, obj)) 
                    self.count = self.count + 1    
                else: 
                    print("Element not inserted. The table is full.")
                
    def isempty(self):
        """
            Purpose: Check if the given table is empty.
            Parameters: -
            Returns: True if the table is empty; False otherwise.
            Comment: -
        """
        return self.count == 0
        
    def lookup(self, key):
        """
            Purpose: Search for a given key and see if it exists in the table
            Parameters: key - The key to be searched in the table.
            Returns: A tuple containing True and the value of the given object 
                     if the given key is found, or False and None if it does not 
                     exist.
            Comment: If the table is empty then (False, None) is returned.
        """
        pos = self._table.low()[0]
        while pos < self.count:
            (newKey, newVal) = self._table.inspectValue((pos,))
            if newKey == key:
                return (True, newVal)
            pos = pos + 1
        return (False, None)        

    def remove(self, key):
        """
            Purpose: Remove a given key, if it exists, from the table.
            Parameters: key - The key to be removed from the table.
            Returns: -
            Comment: The gap that is formed when removing an element in the table
                     is filled by moving the last element in the table to the gap. 
                     If an element is removed from the table then the count is 
                     decreased by 1.
        """        
        if not self.isempty():
            pos = self._table.low()[0]
            found = False
            while not found and pos < self.count:
                (newKey, newVal) = self._table.inspectValue((pos,))
                if newKey == key:
                    self._table.setValue((pos,), self._table.inspectValue((self.count - 1,)))
                    self._table.setValue((self.count - 1,), self._table.inspectValue((self.count,))) 
                    found = True
                pos = pos + 1   
                
            if found: 
                self.count = self.count - 1                   