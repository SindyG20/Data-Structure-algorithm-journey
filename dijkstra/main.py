#Creating dictionary to store the  graph

graph = {
    "A" : {"D": 2, "C": 3},
    "C" : {"D": 1, "E": 5},
    "D" : {"E": 3, "F": 6},
    "E" : {"B": 4, "F": 2},
    "F" : {"B": 7},
    "B" : {}
}

#Distances from the starting point to the node, in a dictionary
#float("inf") - float infinity because we havent yet 
# started reading the graph so for no its still seem as infintiy

distances = {
    "A" : 0, #FROM A to A
    "C" : float("inf"),
    "D" : float("inf"),
    "E" : float("inf"),
    "F" : float("inf"),
    "B" : float("inf")
}