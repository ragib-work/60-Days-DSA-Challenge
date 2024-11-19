"""

Problem Statement:

Given an array of integers "nums" and an integer "target", 
return the number of times target appears in the array.

----------------------------------------------------------------

Example:
Input: nums = [1, 2, 3, 2, 2, 4], target = 2
Output: 3

Explanation:
The number 2 appears 3 times in the array.

"""
# SOLUTIONS:


nums = list(map(int, input("Enter the numbers seprated by Space: ").split()))
target = int(input("Enter the target value: "))


# <-------- My FiRsT ApPrOaCh ------> <----- WiThOuT InBuIlT MeThOd ------->

# def count_occurrence(nums, target):
#     count = 0
#     n = len(nums)
#     for i in range(n):
#         if nums[i]==target:
#             count+=1
#     print(f"{target} appears {count} time in nums")

# count_occurrence(nums, target)

# <------------------- But Slightly we can do better this solution -------------------------------->

# def count_occurrence(nums, target):
#     count = 0
#     for num in nums:
#         if num == target:
#             count+=1
#     print(f"{target} appears {count} time in nums")

# count_occurrence(nums, target)    

# <==============================================================================>

# <------------- SeCoNd ApPrOaCh ---------> <------ UsInG InBuIlT MeThOd -------->

def count_occurrence(nums, target):
    occurrence = nums.count(target)
    print(f"{target} appears {occurrence} time in nums")

count_occurrence(nums, target)



