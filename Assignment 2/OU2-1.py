# -*- coding: utf-8 -*-
# Written by Rasmus Säfvenberg <rasmus.safvenberg@umu.se>
# May be used in the course Datastrukturer och Algoritmer (Python) at Umeå University.
# Usage exept those listed above requires permission by the author.
"""
The purpose of this code is to print the content of an list, which is done 
by reading data from a given file, going through all rows in the data and 
storing each row in the list. The list is then printed element by element.
"""

from ListAsArray import List
#from ListAsTwoCell import List

def printList(lst):
    """
    Purpose: Print all elements in a list, one per line.
    Parameters: lst - An instance of a list.
    Returns: - 
    Comment: -
    """    
    pos = lst.first()
    if pos == lst.end():
        print("The list is empty.")
    
    while pos != lst.end():
        print(lst.inspect(pos))
        pos = lst.next(pos)    

def read_and_store_data(filename, lst):
    """
    Purpose: Read data from a given file and store the data in a list.
    Parameters: filename - the name of the file to read data from.
                lst - the name of the list to store data in.
    Returns: - 
    Comment: The file should contain values that can be converted to float.
    """       
    data = open(filename, "r")
    for row in data:
        pos = lst.end()
        if "\n" in row or "\t" in row:
            row = row.strip("\n")
            row = row.strip("\t")
        
        lst.insert(pos, float(row))
        if pos !=  lst.first():
            pos = lst.previous(pos)
      
    data.close() 

######## MAIN PROGRAM ################

L = List() 

filename = input("Enter the name of the file: ") 

read_and_store_data(filename, L) 
        
printList(L) 