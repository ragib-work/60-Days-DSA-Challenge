"""

Title: Count Unique and Duplicate Numbers

Problem Statement:-
Given an array of integers where each number is between 1 and 100 (inclusive), 
write a function that returns:
The count of numbers that appear exactly once (unique numbers)
The count of numbers that appear more than once (duplicate numbers)

------------------------------------------------------------------------------------

Example 1:

Input: [1, 2, 3, 2, 4, 4, 5]
Output: [3, 2]
Explanation: 
- Numbers appearing once (unique): 1, 3, 5 (count = 3)
- Numbers appearing more than once (duplicates): 2, 4 (count = 2)

Example 2:

Input: [1, 1, 1, 1]
Output: [0, 1]
Explanation:
- No numbers appear once (count = 0)
- Only 1 appears multiple times (count = 1)

"""

# SoLuTiOn:

arr = list(map(int, input("Enter Element Seprated by Space: ").split()))

# <-------- My FiRsT ApPrOaCh ----------> <---------- WiThOuT InBuIlT MeThOd ----------->

# def count_unique_and_duplicate(arr):
#     unique = [arr[0]]
#     duplicate = []
#     l = len(arr)
#     for i in range(1,l):
#         if arr[i] in unique :
#             unique.remove(arr[i])
#             if arr[i] not in duplicate:
#                 duplicate.append(arr[i])
#         elif arr[i] not in duplicate:
#             unique.append(arr[i])
#     print("Unique: ", unique)
#     print("Duplicate: ", duplicate)
#     return [len(unique), len(duplicate)]

# print(count_unique_and_duplicate(arr))


# <========================================== SECOND APPROACH ========================================>

#<----------------------------------- OpTiMal ApPrOaCh -------------------------------------------->

def count_unique_and_duplicate(arr):
    
    l = len(arr)
    
    # Initialize count array with all zeros (size 101 for numbers 1-100)
    count = [0] * 101

    for num in arr:
        count[num] = count[num] + 1
    
    unique_count = 0
    duplicate_count = 0

    for frequency in count:
        if frequency == 1:
            unique_count += 1
        elif frequency > 1:
            duplicate_count += 1
    return [unique_count, duplicate_count]

print(count_unique_and_duplicate(arr))

# Explanation :- 
"""
Steps of Working with the Count Array
1. Initialization
count = [0] * 101

This creates an array of size 101 (to represent numbers 1 through 100).
Initially, all values are 0 because no numbers have been counted yet.
Think of it as:
Index:   0   1   2   3   4   5  ...  100
Count:   0   0   0   0   0   0  ...   0

2. Updating the Count Array
For every number in the input array arr, you increase the value at the corresponding index in count.

Example:
Input: arr = [1, 2, 2, 5, 100]

Process the first number (num = 1):
Increment count[1]:
Index:   0   1   2   3   4   5  ...  100
Count:   0   1   0   0   0   0  ...   0


Process the second number (num = 2):
Increment count[2]:
Index:   0   1   2   3   4   5  ...  100
Count:   0   1   1   0   0   0  ...   0


Process the third number (num = 2 again):
Increment count[2] again:
Index:   0   1   2   3   4   5  ...  100
Count:   0   1   2   0   0   0  ...   0

Note : Index of count array are denoting the numbers , and there values denoting as frequency,
       that means how many times that number occurs.

"""