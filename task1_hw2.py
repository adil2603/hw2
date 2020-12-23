my_list = [1, False, 'Book', 9.5, (1+2j), [1, 2, 3], {1, 2, 3},
           {5: 'five', 2: 'two'}, b"some text", (1, 2, 3), None]

for index, value in enumerate(my_list):
    print(f"{index}. {value} - {type(value)}")
