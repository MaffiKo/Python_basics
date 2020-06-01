translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
for_new_text = []

with open("text_4.txt", "r", encoding="utf-8") as text:
    content = text.read().split("\n")
    for i in content:
        i = i.split(' ', 1)
        for_new_text.append(translate[i[0]] + ' ' + i[1])
    print(for_new_text)

with open("new_text_4.txt", "w+", encoding="utf-8") as new_text:
    print(for_new_text, file=new_text)


#  Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#  При этом английские числительные должны заменяться на русские.
#  Новый блок строк должен записываться в новый текстовый файл.