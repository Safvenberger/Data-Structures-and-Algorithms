# -*- coding: utf-8 -*-
# Written by Rasmus Säfvenberg <rasmus.safvenberg@umu.se>
# May be used in the course Datastrukturer och Algoritmer (Python) at Umeå University.
# Usage exept those listed above requires permission by the author.
"""
The purpose of this code is to implement two sorting algorithms that can be used
to sort the data in a list. 
"""

from ListAsArray import List 
#from ListAsTwoCell import List
import copy 

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
    Purpose: Read data from a given file and store the data in a List.
    Parameters: filename - the name of the file to read data from
                lst - the name of the list to store data in
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


def bubble_sort(lst, cmpfunction): 
    """
    Purpose: Sort data with the use of the bubble sort algorithm.
    Parameters: lst - a list with data to be sorted
                cmpfunction - a function that compares two values. 
                Available options are: greater_than or less_than.
    Returns: A list where the data is sorted according to the specified function
    Comment: A deep copy is made of the list so that the original list remains 
             unsorted.
    """        
    bubble_lst = copy.deepcopy(lst) 
    swapped = True   

    while swapped:
        swapped = False
        pos = bubble_lst.first()

        while pos != bubble_lst.previous(bubble_lst.end()):
            val1 = bubble_lst.inspect(pos)
            val2 = bubble_lst.inspect(bubble_lst.next(pos))
            if cmpfunction(val1, val2):
                temp = bubble_lst.remove(pos)
                bubble_lst.insert(bubble_lst.next(temp), val1)
                swapped = True
            pos = bubble_lst.next(pos)

    return bubble_lst

def split_list(lst):
    """
    Purpose: Split a list into two equally sized parts
    Parameters: lst - a list with data to to be split
    Returns: L1 - the part containing the elements from odd positions (1,3,5,...)
             L2 - the part containing the elements from even positions (2,4,6,...)
    Comment: If the list has an odd amount of elements one of the splits will  
             have one more element than the other.
    """      
    pos = lst.first()    
    L1 = List()
    L2 = List()
    
    while pos != lst.end():
        L1.insert(L1.end(), lst.inspect(pos))
        if lst.next(pos) == lst.end():
            break
        L2.insert(L2.end(), lst.inspect(lst.next(pos)))
        pos = lst.next(lst.next(pos))
        
    return L1, L2

def merge(S1, S2, cmpfunction):
    """
    Purpose: Combine together two lists and sort them by their values
    Parameters: S1 - A list to be combined with S2.
                S2 - A list to be combined with S1.
                cmpfunction - a function that compares two values. 
                Available options are: greater_than or less_than.
    Returns: The combined list of S1 and S2 with sorted values. 
    Comment: The sorting method is decided by cmpfunction and can be either
             ascending or descending. 
             If one of the lists S1, S2 are empty the other one is returned.
    """      
    if S1.isempty() or S2.isempty():
        return S1 or S2
 
    S = List()
    while not S1.isempty() and not S2.isempty():
        if cmpfunction(S1.inspect(S1.first()), S2.inspect(S2.first())):       
            S.insert(S.end(), S2.inspect(S2.first()))
            S2.remove(S2.first())            
        else:
            S.insert(S.end(), S1.inspect(S1.first()))
            S1.remove(S1.first())            
            
    while not S1.isempty():
            S.insert(S.end(), S1.inspect(S1.first()))
            S1.remove(S1.first())
   
    while not S2.isempty():
            S.insert(S.end(), S2.inspect(S2.first()))
            S2.remove(S2.first())
 
    return S
   
def merge_sort(lst, cmpfunction):
    """
    Purpose: Sort data recursively with the use of the merge sort algorithm.
    Parameters: lst - A list to be sorted. 
                cmpfunction - a function that compares two values. 
                Available options are: greater_than or less_than.
    Returns: A list with sorted values. 
    Comment: If the list is empty or has one element th
    """      
    if not lst.isempty() and lst.next(lst.first()) != lst.end(): 
        S1, S2 = split_list(lst)
        S1 = merge_sort(S1, cmpfunction)
        S2 = merge_sort(S2, cmpfunction)        
        lst = merge(S1, S2, cmpfunction)
    return lst
    
def greater_than(val1, val2):
    """
    Purpose: Check if the first value is greater than the second.
    Parameters: val1 - The first value to use for comparison. 
                val2 - The second value to use for comparison. 
    Returns: A boolean value; True if the first value is greater than 
             the second value and False otherwise.
    Comment: val1 and val2 have to be able to be compared. Recommended is to 
             have val1 and val2 as float values.
    """      
    result = False
    if val1 > val2:
        result = True
    return result

def less_than(val1, val2):
    """
    Purpose: Check if the first value is less than the second.
    Parameters: val1 - The first value to use for comparison. 
                val2 - The second value to use for comparison. 
    Returns: A boolean value; True if the first value is less than 
             the second value and False otherwise.
    Comment: val1 and val2 have to be able to be compared. Recommended is to 
             have val1 and val2 as float values.
    """      
    result = False
    if val1 < val2:
        result = True
    return result    

############### MAIN PROGRAM ##########################

L = List()

filename = input("Enter the name of the file: ") 

read_and_store_data(filename, L)

allowed_inputs = ["1", "2", "3", "4", "5"]
user_input = ""
menu_text = ("What do you want to do? Enter: \n" + 
             "1 for bubble sort (descending order) \n" + 
             "2 for bubble sort (ascending order) \n" +
             "3 for merge sort (descending order) \n" +
             "4 for merge sort (ascending order) \n" +
             "5 to exit the program. ")

while user_input not in allowed_inputs:
    user_input = input(menu_text)
    print("")
    while user_input in allowed_inputs:
        if user_input ==  "5":
            print("The program is closing.")
            break   
        
        print("Original: ") 
        printList(L)
        print("")
        
        method = "List sorted by bubble sort: "
        
        if user_input == "1":
            sorted_list = bubble_sort(L, less_than)
        elif user_input == "2":
            sorted_list = bubble_sort(L, greater_than)
        elif user_input == "3":
            sorted_list = merge_sort(L, less_than)
            method = "List sorted by merge sort: "
        elif user_input == "4":
            sorted_list = merge_sort(L, greater_than)
            method = "List sorted by merge sort: "

        print(method)
        printList(sorted_list)
        print("")
        user_input = input(menu_text)
        print("")