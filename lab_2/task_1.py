numbers = [1, 2, 3, 4, 5]

def sum_for(nums):
    c = 0
    for num in nums:
        c+= num
    return c

def sum_while(nums):
    c = 0
    i = 0
    while i < len(nums):
        c += nums[i]
        i += 1
    return c

def sum_recursion(nums):
    if not nums:
        return 0
    return nums[0] + sum_recursion(nums[1:])


print("1:", sum_for(numbers))
print("2:", sum_while(numbers))
print("3:", sum_recursion(numbers))