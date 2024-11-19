"""

PROBLEM STATEMENT: Print Alternate Elements of an Array

You are given an array of integers. Your task is to print the alternate elements of the array, 
starting with the first element.

----------------------------------------------------------------------------------

OUTPUT FORMAT:
Print the alternate elements of the array, each element separated by a space.

------------------------------------------------------------------------------------

EXAMPLE:

Example 1:

Input:
5
1 2 3 4 5

Output:
1 3 5

Example 2:

Input:
6
10 20 30 40 50 60

Output:
10 30 50

"""

# SOLUTION :-

# First Approach 
arr = list(map(int, input("Enter Elements of an Array followed by space:- ").split()))
# def print_alternate(arr):
#     n = len(arr)
#     for i in range(0,n,2):
#         print(arr[i], end=" ")

# print_alternate(arr)

# <----------------------------------------------------------------------------------->

# Second Approach 
def print_alternate(arr):
    n = len(arr)
    print(*arr[::2])

print_alternate(arr)