"""

PROBLEM STATEMENT: Create a Duplicate of an Array

You are given an array of integers. Your task is to create a duplicate of the array 
and print both the original and the duplicate array.

-----------------------------------------------------------------------------

OUTPUT FORMAT:
Print the elements of the original array followed by the elements of the duplicate array, 
each element separated by a space.

EXAMPLE:

Example 1:

Input:
5
1 2 3 4 5

Output:
Original Array: 1 2 3 4 5
Duplicate Array: 1 2 3 4 5

Example 2:

Input:
4
7 8 9 10

Output:
Original Array: 7 8 9 10
Duplicate Array: 7 8 9 10

"""

# SOLUTION :- 

# First Way Solution :-
arr = list(map(int, input("Enter Element Followed By Space:- ").split()))
# def duplicate_arry(arr):
#     n = len(arr)
#     duplicate_arr = []
#     for i in range(n):
#         duplicate_arr.append(arr[i])
#     print("Original Array: ", *arr)
#     print("Duplicate Array: ", *duplicate_arr)

# duplicate_arry(arr)

# <------------------------------------------------------------------------------------------------->

# Second Way Solution:- 
def duplicate_array(arr):
    
    # Copy array from Original Array "arr"
    duplicate_arr = arr[:]
    print("Original Array: ", *arr)
    print("Duplicate Array: ", *duplicate_arr)

duplicate_array(arr)
