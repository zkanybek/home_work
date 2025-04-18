# Big O натация
from turtledemo.penrose import start


# O(1)

def get_element(arr, index):
    return arr[index]
print(get_element([1,2,3,4,5,6,7,8,9,0], 6))

# O(log n)

import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
        return -1


arr = [1, 3, 5, 7, 9, 45, 56]

target = 4

print(binary_search(arr, target))

# O(n)
# arr = [1, 2, 3, 5, 7, 9, 11, 13]
target = 7
def find_element(arr, target):

    for i, value in arr:
        if value == target:
            return 1
    return 'Not'

target = 999999
arr = list(range(100000000))

start_1 = time()


arr = [1, 3, 5, 7, 9, 45, 56]
target = 5

print(find_element(arr, target))

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
           if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5, 1, 4, 6, 9]

# print(bubble_sort(arr)





# nums = [2, 7, 11, 15]  цель = 9

nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    num_map = {}

    for index, num in enumerate(nums):
        complement  = target - num
        if complement in num_map:
            return  [num_map[complement], index]
        num_map[num] = index