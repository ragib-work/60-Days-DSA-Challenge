"""

Title: Two Sum Target Check

Problem Statement:
Given an array of integers and a target value, write a function that determines 
if there exist any two different elements in the array that add up to the target value. 
Return true if such a pair exists, false otherwise.

----------------------------------------------------------------------------------------
Example 1:
Input: 
array = [2, 7, 11, 15]
target = 9
Output: true
Explanation: 2 + 7 = 9, so we return true

Example 2:
Input:
array = [3, 5, 8, 1]
target = 4
Output: false
Explanation: No two different elements in the array sum to 4

Example 3:
Input:
array = [5, 5]
target = 10
Output: true
Explanation: 5 + 5 = 10

Constraints:
Array length is at least 2
Array can contain both positive and negative integers
The same element can be used twice if it appears twice in the array
Array can have duplicate elements

"""

# SOLUTION:-

nums = list(map(int, input("Enter the numbers seprated by Space: ").split()))
target = int(input("Enter the target value: "))

# <-------- My FiRsT ApPrOaCh ----------> <---------- WiThOuT InBuIlT MeThOd ----------->

def check_target_sum(arr, target):
    
    l = len(arr)
    for i in range(l):
        for j in range(i+1, l):
            if arr[i]+arr[j] == target:
                return True
    
    return False

print(check_target_sum(nums, target))
