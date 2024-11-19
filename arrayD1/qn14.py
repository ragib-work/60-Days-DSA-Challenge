"""

Title: Find Second Maximum Element

Problem Statement:
Write a function that finds the second largest element in an array of integers. 
If no second largest element exists (either because array has less than 
2 unique elements), return -1.

----------------------------------------------------------------------------


Example 1:
Input: [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element is 35, and second largest is 34


Example 2:
Input: [10, 10, 10]
Output: -1
Explanation: All elements are same, so no second largest exists


Example 3:
Input: [5]
Output: -1
Explanation: Array has only one element, so no second largest exists


Example 4:
Input: [-1, -2, -3, -4]
Output: -2
Explanation: -1 is largest and -2 is second largest


Constraints:

Array length is at least 1
Array can contain both positive and negative integers
Array can have duplicate elements
Return -1 if no second largest element exists
Second largest should be strictly less than the largest element

"""


# SOLUTION:-

nums = list(map(int, input("Enter the numbers seprated by Space: ").split()))

# <---------- NoT My ApPrOaCh -------------> <-------- By ClAuDe Ai ----------->

def find_second_max(arr):
    
  # If array has less than 2 elements
    l = len(arr)
    if l<2:
        return -1
    
  # Initialize with negative infinity
    first_max = float('-inf')
    second_max = float('-inf')

  # First pass to find maximum
    for num in arr:
        if num > first_max:
            first_max = num


  # Check if all elements are same  
    all_same = True
    for num in arr:
        if num != first_max:
            all_same = False
    
    if all_same:
        return -1
    
    
  # Second pass to find second maximum
    for num in arr:
        if num > second_max and num < first_max:
            second_max = num
    
    return second_max