def repeat(numbers):
    s = set()
    result = []
    for num in numbers:
        if num in s:
            result.append("YES")
        else:
            result.append("NO")
            s.add(num)

    return result


# Пример использования
input_numbers = "1 2 3 4 5 2 3 6"
numbers_list = input_numbers.split()
print("Результат:", repeat(numbers_list))