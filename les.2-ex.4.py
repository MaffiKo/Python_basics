user_str = str(input("Напишите маленькое предложение (2-3 слова) без знаков пунктуации - "))
enter = ()
max_word = 10
num_str = 1

for n in range(user_str.count(" ") + 1):
    my_word = user_str.split()
    if len(str(my_word)) <= max_word:
        print(f" {num_str} {my_word [n]}")
        num_str += 1
    else:
        print(f" {num_str} {my_word [n] [0:max_word]}")
        num_str += 1

#  4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
#  Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
#  Если в слово длинное, выводить только первые 10 букв в слове.