"""

Title: Three Sum Target Check

Problem Statement:
Given an array of integers and a target value, write a function 
that determines if there exist any three different elements in 
the array that add up to the target value. Return true if such 
a triplet exists, false otherwise.

---------------------------------------------------------------

EXAMPLES:-

Example 1:
Input: 
array = [1, 4, 45, 6, 10, 8]
target = 22
Output: true
Explanation: 4 + 10 + 8 = 22, so we return true

Example 2:
Input:
array = [1, 2, 3, 4, 5]
target = 15
Output: false
Explanation: No three elements in the array sum to 15

Example 3:
Input:
array = [5, 5, 5]
target = 15
Output: true
Explanation: 5 + 5 + 5 = 15

Constraints:-
Array length is at least 3
Array can contain both positive and negative integers
Array can have duplicate elements
Three different array positions must be used (even if values are same)

"""

# SOLUTION:-

nums = list(map(int, input("Enter the numbers seprated by Space: ").split()))
target = int(input("Enter the target value: "))

# <-------- My FiRsT ApPrOaCh ----------> <---------- WiThOuT InBuIlT MeThOd ----------->

def check_target_sum(arr, target):
    
    n = len(arr)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==target:
                    print (arr[i],arr[j],arr[k])
                    return True
    return False

print(check_target_sum(nums,target))