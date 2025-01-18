"""SDET Interview | Coding Round | #Code7
Write a Python function that takes a list of integers and moves all the zeroes to the end while maintaining the relative order of the non-zero elements. The function should modify the list in place and return the modified list.
#SDET #automationtesting #coding #pythonprogramming #pythoncode
"""

def move_zeroes(nums):
    zeroes = 0
    for num in nums:
        if num == 0:
            nums.remove(num)
            zeroes +=1
    for _ in range(zeroes):
        nums.insert(0,0)
    return nums

def move_zeroes_second(arr):

    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero_index] = arr[non_zero_index],arr[i]
            non_zero_index +=1
    return arr