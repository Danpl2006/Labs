def count(s):
    c = {}
    for char in s:
        if char in c:
            c[char] += 1
        else:
            c[char] = 1
    return c

text = "hello world"
print("Количество вхождений символов:", count(text))