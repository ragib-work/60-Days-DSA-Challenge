"""

PROBLEM STATEMENT: Create Two Arrays for Odd and Even Elements

You are given an array of integers. Your task is to create two separate arrays:
One array containing all the odd elements from the input array.
Another array containing all the even elements from the input array.

-------------------------------------------------------------------------------------------

OUTPUT FORMAT:
Print the two arrays:

First, print the array containing odd elements.
Then, print the array containing even elements.
Each array's elements should be separated by a space.

--------------------------------------------------------------------------------------------

EXAMPLES:

Example 1:

Input:
6
1 2 3 4 5 6

Output:
Odd Array: 1 3 5
Even Array: 2 4 6

Example 2:

Input:
7
10 21 30 43 55 66 77

Output:
Odd Array: 21 43 55 77
Even Array: 10 30 66

"""

# SOLUTION:-

arr = list(map(int, input("Enter Element Seprated by Space: ").split()))

# First Approach :- 
# def odd_even_array(arr):
#     even = []
#     odd = []
#     for elem in arr:
#         if elem%2==0:
#             even.append(elem)
#         else:
#             odd.append(elem)
#     print("Odd Array: ",*odd)
#     print("Even Array: ", *even)


# Second Approach:-
def odd_even_array(arr):
    odd = [x for x in arr if x%2!=0]
    even = [x for x in arr if x%2==0]
    print("Odd Array: ", *odd)
    print("Even Array: ", *even)

odd_even_array(arr)