import random

def f(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] < 0:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
    return nums

random_list = [random.randint(-10, 10) for _ in range(10)]
print("Исходный список:", random_list)
print("После:",f(random_list))