"""
Given an array of integers, find the maximum sum of a contiguous subarray. The subarray must contain at least one element. Write a function that computes this sum efficiently.

Function Description
Complete the function max_continuous_sum in the editor below.

max_continuous_sum has the following parameter(s):

int arr[n]: An array of integers.
Returns:

int: The maximum sum of a contiguous subarray.
Constraints
1
≤
𝑛
≤
1
0
6
1≤n≤10
6
  (Length of the array)
−
1
0
4
≤
𝑎
𝑟
𝑟
[
𝑖
]
≤
1
0
4
−10
4
 ≤arr[i]≤10
4
  (Each element of the array)
Input Format
The first line contains a single integer,
𝑛
n, the size of the array.
The second line contains
𝑛
n space-separated integers, representing the elements of the array.

Output Format
Output a single integer, the maximum sum of a contiguous subarray
"""



def largest_continous_sum(arr):
    if len(arr) == 0:
        return 0

    curr_sum = arr[0] # take current sum and max sum values which
    max_sum = arr[0] # is first element of the
    for num in arr[1:]:
        curr_sum += num # Define Current Sum curr_sum = current_sum + num
        #curr_sum = max(num, curr_sum+num)
        if num > curr_sum: # If Num is greater than  curr_sum
            curr_sum = num
        if max_sum < curr_sum: # If max_sum is < curr_sum
            max_sum = curr_sum
    return max_sum


if __name__ == "__main__":
    # Example 1: Mixed +ve and -ve numbers
    arr1= [-2,1,-3,1,8,8]
    print(largest_continous_sum(arr1))