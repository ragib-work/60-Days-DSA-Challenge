"""

Title: Insert Element at Position X

Problem Statement:
Write a function that inserts an element at position X in an array, 
shifting all existing elements from position X onwards to the right by one position. 
If X is greater than the array length, insert at the end. 
The array should grow in size by 1 after insertion.

--------------------------------------------------------------------------

Example 1:
Input: 
array = [1, 2, 3, 4, 5]
element = 10
position = 2
Output: [1, 2, 10, 3, 4, 5]
Explanation: 10 is inserted at index 2, shifting 3, 4, and 5 to the right

Example 2:
Input:
array = [5, 6, 7]
element = 8
position = 0
Output: [8, 5, 6, 7]
Explanation: 8 is inserted at beginning, shifting all elements right

Example 3:
Input:
array = [1, 2, 3]
element = 4
position = 5
Output: [1, 2, 3, 4]
Explanation: Since position 5 > array length, element is inserted at end

Example 4:
Input:
array = []
element = 1
position = 0
Output: [1]
Explanation: Inserting into empty array at position 0


Constraints:

Position X is non-negative integer
Array can be empty
If X > array length, insert at end
Array elements can be any integer
No size limit on the array

"""

# SOLUTION:-

nums = list(map(int, input("Enter the numbers seprated by Space: ").split()))
element = int(input("Enter the value of Element: "))
idx = int(input("Enter Where You Want to Insert: "))

# <------- My FiRsT ApPrOaCh -------> <----- WiThOuT InBuIlT MeThOd ----->

def insert_elem(arr, idx, element):

    arr.append(None)
    n = len(arr)
    for i in range(n-2, idx-1, -1):
        arr[i+1] = arr[i]
    
    arr[idx] = element
    print("arr: ",arr)

insert_elem(nums, idx, element)