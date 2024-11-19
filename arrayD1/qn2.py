"""
PROBLEM STATEMENT:- Print Array Elements in Reverse Order

You are given an array of integers. Your task is to print 
the elements of the array in reverse order.

------------------------------------------------------------------

OUTPUT FORMAT :-
Print the elements of the array in reverse order, each element separated by a space.

EXAMPLE:

Example 1:

input:
5
1 2 3 4 5

output:
5 4 3 2 1

"""

# SOLUTION :-

#First Approach :-
# arr = map(int,input("Enter the elements of an Arrays seperated by comma (,): ").split(","))
# li = list(arr)
# n = len(li)
# def print_reverse(li):
#     for i in range( n-1 , -1, -1 ):
#         print(li[i], sep=",", end=" ")    
#     print()
# print_reverse(li)

# <-------------------------------------------------------------------------------------------->

#Second Approach :- 
arr = list(map(int, input("Enter Number Seprated by Space: ").split()))
def print_reverse(arr):
    n = len(arr)
    print(*arr[::-1])

print_reverse(arr)