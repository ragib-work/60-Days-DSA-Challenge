"""

Title: Find Minimum Element in Array

Problem Statement:
Write a function that finds the minimum element in an array of integers. 
The function should return the smallest value present in the array.

------------------------------------------------------------------------

Example 1:
Input: [1, 4, 3, 8, 5]
Output: 1
Explanation: 1 is the largest element in the array

Example 2:
Input: [-5, -2, -10, -1]
Output: -10
Explanation: -10 is the largest element in the array of negative numbers

"""

# SOLUTION:-

nums = list(map(int, input("Enter the numbers seprated by Space: ").split()))

# <-------- My FiRsT ApPrOaCh ----------> <---------- WiThOuT InBuIlT MeThOd ----------->

def find_min(arr):
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num

print("Min Num: " , find_min(nums))
