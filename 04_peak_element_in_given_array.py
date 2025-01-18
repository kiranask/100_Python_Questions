"""
A peak element in an array is an element that is strictly greater than its neighbors. Given a 0-indexed integer array nums, your task is to find a peak element and return its index. If the array contains multiple peaks, return the index of any one of the peaks. You may assume that nums[-1] = -∞ and nums[n] = -∞, where n is the length of the array.

Example 1:

vbnet
Copy
Edit
Input: nums = [1, 2, 3, 1]
Output: 2
Explanation: 3 is a peak element, and your function should return the index numbe


Solution tip: Use binary Search.

Tips to remember

start   mid   mid+1   end

if mid > mid+1

end = mid

else
start = mid +1


"""

def findPeakElement(self, arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return 0
    # Use Binary Search
    start, end = 0, len(arr) - 1
    while end > start:
        mid = (start + end) // 2

        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return start