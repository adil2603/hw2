my_list = input("Ввседите числа списка через пробел: ").split()
print("Введенны текст: ", my_list)

idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1

my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
print("Измененный текст: ", my_list)