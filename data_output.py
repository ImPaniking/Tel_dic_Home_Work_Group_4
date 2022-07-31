from tkinter import *

from worck_with_base import take_from_base as TAKE

phone_dic = TAKE()

# сюда надо передавать номер записи в словаре
dict_number = '1'

for item in phone_dic[dict_number].values():
    if type(item) == dict:
        target_data = item.items()

data_personal_list = []

for item in phone_dic[dict_number].items():
    if item[0] == 'Second name':
        data_personal_list.append(item[1])
    if item[0] == 'First name':
        data_personal_list.append(item[1])
    if item[0] == 'Othen name':
        data_personal_list.append(item[1])
    if item[0] == 'Type of Contact':
        data_personal_list.append(item[1])
    if item[0] == 'Company':
        data_personal_list.append(item[1])
    if item[0] == 'Sex':
        data_personal_list.append(item[1])
    if item[0] == 'Birth Day':
        data_personal_list.append(item[1])
    if item[0] == 'Comment':
        data_personal_list.append(item[1])

data_telefon_list = []
for item in target_data:
    if item[0] == 'Telefon type':
        data_telefon_list.append(item[1])
    if item[0] == 'Telefon number':
        data_telefon_list.append(item[1])

data_personal_list.insert(4, data_telefon_list[0])
data_personal_list.insert(5, data_telefon_list[1])


window = Tk()
window.title('Информационная карточка')

titles_list = ['Фамилия:', 'Имя:', 'Отчество:', 'Прочее (ник или лишние слова):', \
               'Компания:', 'Тип:', 'Телефон:', 'Пол:', \
               'Год рождения:', 'Комментарий:']

for i in range(len(titles_list)):

    for y in range(2):
        if y == 0:
            Message(width=300, text=person_info[i+1]) \
                .grid(row=i, column=y, sticky=W)
        else:
            Message(width=300, text=data_personal_list[i]) \

                .grid(row=i, column=y)

window.mainloop()
