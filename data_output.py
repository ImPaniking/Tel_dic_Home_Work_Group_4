from tkinter import *

window = Tk()
window.title('Информационная карточка')

titles_list = ['Фамилия:', 'Имя:', 'Отчество:', 'Прочее (ник или лишние слова):', \
               'Компания:', 'Тип:', 'Телефон:', 'Пол:', \
               'Год рождения:', 'Комментарий:']

# data_list = [] - создание списка со строками, для внесения их в карточку вывода

for i in range(len(titles_list)):
    for y in range(2):
        if y == 0:
            Message(width=300, text=titles_list[i]) \
                .grid(row=i, column=y, sticky=W)
        else:
            Message(text='1') \
                .grid(row=i, column=y)


window.mainloop()
