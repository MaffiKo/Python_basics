with open("first_hw.txt", "w+", encoding='utf-8') as create_file:
    line_num = 1
    while True:
        str_list = input('Enter the data or click "ENTER" for exit: ')
        if str_list:
            create_file.writelines(f'{str_list}\n')
            line_num += 1
        else:
            line_num -= 1
            break
    print(f"\nTotal lines: {line_num}")
    create_file.seek(0)
    content = str(create_file.read()).split('\n')
    content.pop(-1)

    n = 1
    while True:
        if line_num > 0:
            print(f"Line num {n} got {len(content[n - 1])} character(s)")
            line_num -= 1
            n += 1
        else:
            break

#  Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.
#  +2е Создать текстовый файл (не программно), сохранить в нем несколько строк
#  выполнить подсчет количества строк, количества слов в каждой строке.
