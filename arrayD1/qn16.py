"""

Title: Delete Element at Position X

Problem Statement:
Write a function that delete an element at position X in an array, 
shifting all existing elements from position X backwars to the left by one position. 
The array should reduce in size by 1 after deletion.

"""

# SOLUTION:-

nums = list(map(int, input("Enter the numbers seprated by Space: ").split()))
idx = int(input("Enter Where You Want to Delete: "))

# <------- My FiRsT ApPrOaCh -------> <----- WiThOuT InBuIlT MeThOd ----->

def delete_elem(arr, idx):

    n = len(arr)
    for i in range(idx,n-1):
        arr[i] = arr[i+1]
    
    arr.pop()
    print("arr: ",arr)

delete_elem(nums,idx)
