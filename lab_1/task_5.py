s = input("Введите строку: ")
s = s.replace(" ", "").replace(",", "")
# приводим строку к нижнему регистру
s = s.lower()
if s == s[::-1]: # сравниваю с развернутой строкой
    print("YES")
else:
    print("NO")