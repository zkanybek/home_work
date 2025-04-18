# from lesson.lesson6 import two_sum

nums = [3, 4, 6, 8, 10, 14]
target =  11

def two_sum(nums, target):
    see = {}
    for index, num in  enumerate(nums):
        answer  = target - num
        if answer in see:
            return [see[answer], index]
        see[num] = index

print(two_sum(nums, target))



