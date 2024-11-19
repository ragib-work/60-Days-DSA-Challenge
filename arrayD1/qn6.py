"""

Problem Statement:

Given an array of integers nums, calculate and return:

1.The sum of all elements in the array.
2.The product of all elements in the array.

------------------------------------------------

Example:
Input: nums = [1, 2, 3, 4]
Output: [10, 24]

Explanation:

Sum = 1 + 2 + 3 + 4 = 10
Product = 1 * 2 * 3 * 4 = 24

"""

arr = list(map(int, input("Enter Elements Sperated by Space: ").split()))
def cal_sum_prod(arr):
    sums = 0
    prods = 1
    for elem in arr:
        sums = sums + elem
        prods = prods*elem
    return sums, prods

sums, prods = cal_sum_prod(arr)
print("Sum: ", sums)
print("Product: ", prods)
    