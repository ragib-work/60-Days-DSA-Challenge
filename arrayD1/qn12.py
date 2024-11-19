"""

Title: Find Maximum Element in Array

Problem Statement:
Write a function that finds the maximum element in an array of integers. 
The function should return the largest value present in the array.

------------------------------------------------------------------------

Example 1:
Input: [1, 4, 3, 8, 5]
Output: 8
Explanation: 8 is the largest element in the array

Example 2:
Input: [-5, -2, -10, -1]
Output: -1
Explanation: -1 is the largest element in the array of negative numbers

Example 3:
Input: [7]
Output: 7
Explanation: In an array with single element, that element is the maximum

Example 4:
Input: [5, 5, 5, 5]
Output: 5
Explanation: When all elements are same, any element is the maximum

"""

# SOLUTION:-

nums = list(map(int, input("Enter the numbers seprated by Space: ").split()))

# <-------- My FiRsT ApPrOaCh ----------> <---------- WiThOuT InBuIlT MeThOd ----------->

def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

print("Max Num: " , find_max(nums))
