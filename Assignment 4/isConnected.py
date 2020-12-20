# -*- coding: utf-8 -*-

# Written by Rasmus Säfvenberg <rasmus.safvenberg@umu.se>.
# May be used in the course Datastrukturer och Algoritmer (Python) at Umeå University.
# Usage exept those listed above requires permission by the author.

"""
The purpose of the code is to examine if there is a path between two given nodes, 
i.e. it is checked if they are connected. The control is done through the help of
a breadth-first traversal of a graph, and checks if we can reach the destination
node from the origin node.
"""
from OneCell import OneCell
from DirectedGraph import Node
from DirectedGraph import DirectedGraph
from DirectedList import DirectedList
from Edge import Edge
import sys

def readDataFromFile(filename):
    """
        Purpose: Read data from a given file. 
        Parameters: filename - the name and extension of the given file.
        Returns: data - A list containing information about the amount of edges, 
                 as well as the nodes and their edges.
        Comment: If the file does not exist or is empty, then an error is thrown.
    """        
    data = []
    try: 
        file = open(filename)
        data = file.read().splitlines()
        file.close()
    except FileNotFoundError:
        sys.exit("The specified file does not exist.")

    if not data:
        sys.exit("The given file does not contain any data.")
        
    try:
        int(data[0]) # Number of nodes should be the first row of the datafile.
    except:
        sys.exit("The given file does not follow the correct format.") 
    
    return data


def equalFunction(n1, n2):
    """
        Purpose: Check if two nodes are equal, i.e. have the same label.
        Parameters: n1 - the first node
                    n2 - the second node
        Returns: Bool; True if the labels are the same. False otherwise.
        Comment: -
    """    
    if str(n1) == str(n2):
        return True
    return False


def fillGraphWithData(data, eqFcn):
    """
        Purpose: Fill a graph with the information stored in a datafile.
        Parameters: data - the nodes and edges to be added to the graph
                    eqFcn - a function to compare if two nodes are equal.                    
        Returns: graph - A graph filled with nodes and edges from the data.
        Comment: There can be at most one direct edge in a given direction between
                 two nodes. If there are more or less than two nodes on a given
                 row an error is thrown. As the first row contains information 
                 about the amount of nodes, it is skipped when adding data to graph.
    """        
    graph = DirectedGraph(eqFcn)
    for row in data[1:]: 
        rowNodes = row.split(" ")  
        if len(rowNodes) == 2: 
            n1 = Node(rowNodes[0]) 
            n2 = Node(rowNodes[1])
            e = Edge(n1, n2)
            graph.insertNode(n1)
            graph.insertEdge(e) 
        else: 
            sys.exit("File is not in the correct format.")  
    return graph
    
    
def breadthFirst(n, graph):
    """
        Purpose: Traverse a graph from node n with a breadth first search.
        Parameters: n - the starting node for the traversal
                    graph - a graph to be traversed
        Returns: visited - a list of the visited nodes. 
        Comment: The traversal continues until a node has been already been seen,
                 i.e. the current node in neighbour also exists in visited. 
                 The list q is used as a queue to utilize the FIFO principle.
    """          
    q = [] # Create a empty list, and use it as a queue.
    q.append(n) # Add to the end of the queue.
    visited = [str(n)] 
    while q: # Repeat as long as the queue is not empty.
        p = q[0]
        q.pop(0) # Remove first element from queue.
        neighbourSet = graph.neighbours(p)
        for neighbour in neighbourSet:
            if str(neighbour) not in visited:
                q.append(neighbour) # Add value to the end of the queue.
                visited.append(str(neighbour))
    return visited


def isConnected(origin, dest, lst):
    """
        Purpose: Check if there is a path between two nodes.
        Parameters: origin - the node to start traversing from
                    dest - the node we want to reach
                    lst - a list containg all the nodes that can be reached from
                          the origin node
        Returns: A printed statement giving the information if there is a path
                 between the nodes origin and dest. 
        Comment: A node is considered connected to itself (origin = destination)
    """         
    found1 = False
    found2 = False
    if origin and dest in lst:
        found1 = True
        found2 = True
    if found1 and found2: 
        print(origin + " and " + dest + " are connected")
    else: 
        print(origin + " and " + dest + " are not connected") 

############################ MAIN PROGRAM ######################################

if len(sys.argv) == 2:
    filename = sys.argv[1]
else: # In case user forgets to provide a file name
    filename = input("Give filename for the file containing nodes and paths: ")  
    
data = readDataFromFile(filename)
g = fillGraphWithData(data, equalFunction)

connection = input("Enter origin and destination (quit to exit): ")

while "quit" not in connection.lower():
    if len(connection.split(" ")) == 2 :
        (origin, destination) = connection.split(" ")
        n = Node(origin)
        l = breadthFirst(n, g)
        isConnected(origin, destination, l)
    else:
        print("Incorrect input. Try again.")
    connection = input("Enter origin and destination (quit to exit): ")    