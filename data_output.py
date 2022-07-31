from tkinter import *
from worck_with_base import take_from_base
from dict import person_info

data = take_from_base()

window = Tk()
window.title('Информационная карточка')

titles_list = ['Фамилия:', 'Имя:', 'Отчество:', 'Прочее (ник или лишние слова):', \
               'Компания:', 'Тип:', 'Телефон:', 'Пол:', \
               'Год рождения:', 'Комментарий:']

# data_list = [] - создание списка со строками, для внесения их в карточку вывода

for i in range(len(data['1'])):
    for y in range(2):
        if y == 0:
            Message(width=300, text=person_info[i+1]) \
                .grid(row=i, column=y, sticky=W)
        else:
            Message(text=data['1'][f'{person_info[i+1]}']) \
                .grid(row=i, column=y)


window.mainloop()
