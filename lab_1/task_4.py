ip = input("Введите IP-адрес: ")
numbers = ip.split('.') # разбиваем строку на части по символу точки

if len(numbers) != 4:
    print("NO")
else:
    for i in numbers:
        if not i.isdigit() or not (0 <= int(i) <= 255): # проверка: все ли символы цифры и находится ли в диапазоне до 255 включительно
            print("NO")
    else:
        print("YES")