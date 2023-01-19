#!/usr/bin/python3
# 
# Returns the neighbors of a value in a 2D Array (Matrix) based on the range given
 
a = [[ 11,  21,  31,  41,  51,  61,  71],
     [ 12,  22,  32,  42,  52,  62,  72],
     [ 13,  23,  33,  43,  53,  63,  73],
     [ 14,  24,  34,  44,  54,  64,  74],
     [ 15,  25,  35,  45,  55,  65,  75],
     [ 16,  26,  36,  46,  56,  66,  76],
     [ 17,  27,  37,  47,  57,  67,  77]]
     

def find_neighbors(radius, row_number, column_number):
     return [[a[i][j] if  i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else 0
                for j in range(column_number-1-radius, column_number+radius)]
                    for i in range(row_number-1-radius, row_number+radius)]                    