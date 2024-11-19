"""

Given an array of integers nums, determine if the array is:

Sorted in non-decreasing order (forward).
Sorted in non-increasing order (backward).
Not sorted at all.

Return:
"Forward" if the array is sorted in non-decreasing order.
"Backward" if the array is sorted in non-increasing order.
"Unsorted" if the array is not sorted.

-------------------------------------------------------------

Examples:

Input: nums = [1, 2, 3, 4]
Output: "Forward"
Explanation: The array is sorted in non-decreasing order.

Input: nums = [4, 3, 2, 1]
Output: "Backward"
Explanation: The array is sorted in non-increasing order.

Input: nums = [1, 3, 2, 4]
Output: "Unsorted"
Explanation: The array is not sorted in either order.

"""

# SoLuTiOn:

arr = list(map(int, input("Enter Element Seprated by Space: ").split()))


# <-------- My FiRsT ApPrOaCh ----------> <---------- WiThOuT InBuIlT MeThOd ----------->

# def check_sorted(arr):
#     min_num = arr[0]
#     max_num = arr[0]
#     is_Sorted = True
#     for elem in arr:
#         if elem>=min_num:
#             min_num = elem
#         else:
#             is_Sorted = False
    
#     if is_Sorted:
#         return "Forward"
#     else:
#         is_Sorted = True
#         for elem in arr:
#             if elem<=max_num:
#                 max_num = elem
#             else:
#                 is_Sorted = False
#         if is_Sorted :
#             return "Backward"
#         else:
#             return "Not Sorted"
        
# print(check_sorted(arr))


# <============================  SECOND APPROACH : OPTIMAL APPROACH ================================>

# <---------------------------- OpTiMaL ApPrOaCh ----------------------------------------->

# def check_shorted(arr):
#     is_forward = True
#     is_backward = True
#     l = len(arr)
#     for i in range(1,l):
#         if arr[i]<arr[i-1]:
#             is_forward = False
#         else :
#             is_backward = False
#     if is_forward:
#         return "Forward"
#     elif is_backward:
#         return "Backward"
#     else:
#         return "Unsorted"

# print("Sorted: ", check_shorted(arr))


#<------------------------------- UsInG InBuIlT MeThOd ------------------------------------------->
def check_sorted(nums):
    if nums == sorted(nums):  # Check forward order
        return "Forward"
    elif nums == sorted(nums, reverse=True):  # Check backward order
        return "Backward"
    else:
        return "Unsorted"

print("Sorted: ", check_sorted(arr))