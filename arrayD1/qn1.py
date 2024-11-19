
"""
PROBLEM STATEMENT:-

You are given an array of integers. Your task is to print each element 
of the array along with its respective index.For each element in the array, 
display the index and the element in a formatted output. 
The index should start from 0, and you should display each element-index pair on a new line.

OUTPUT FORMAT :-
For each element in the array, output a line containing the element's index 
followed by its value, separated by a space.

Example 1

Input:
5
3 8 -1 0 2

Output:
0 3
1 8
2 -1
3 0
4 2

"""


# Solution :-
arr = [3, 8, -1, 0, 2]
for i in range(len(arr)):
    print( i , arr[i]) 

