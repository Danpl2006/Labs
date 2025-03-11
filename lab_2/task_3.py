def count_pairs(nums):
    from collections import defaultdict
    count_dict = defaultdict(int)
    pairs = 0

    for num in nums:
        count_dict[num] += 1

    for key in count_dict:
        pairs += count_dict[key] * (count_dict[key] - 1) // 2

    return pairs

numbers = [1, -1, 2, 3, -5, 1, 2, -8, -9, 2]
print("Количество пар:", count_pairs(numbers))