from tkinter import *

from worck_with_base import take_from_base as TAKE

# phone_dic = TAKE()

# # сюда надо передавать номер записи в словаре
# dict_number = '1'

# for item in phone_dic[dict_number].values():
#     if type(item) == dict:
#         target_data = item.items()

# data_personal_list = []

# for item in phone_dic[dict_number].items():
#     if item[0] == 'Second name':
#         data_personal_list.append(item[1])
#     if item[0] == 'First name':
#         data_personal_list.append(item[1])
#     if item[0] == 'Othen name':
#         data_personal_list.append(item[1])
#     if item[0] == 'Type of Contact':
#         data_personal_list.append(item[1])
#     if item[0] == 'Company':
#         data_personal_list.append(item[1])
#     if item[0] == 'Sex':
#         data_personal_list.append(item[1])
#     if item[0] == 'Birth Day':
#         data_personal_list.append(item[1])
#     if item[0] == 'Comment':
#         data_personal_list.append(item[1])

# data_telefon_list = []
# for item in target_data:
#     if item[0] == 'Telefon type':
#         data_telefon_list.append(item[1])
#     if item[0] == 'Telefon number':
#         data_telefon_list.append(item[1])

# data_personal_list.insert(4, data_telefon_list[0])
# data_personal_list.insert(5, data_telefon_list[1])


# window = Tk()
# window.title('Информационная карточка')

# titles_list = ['Фамилия:', 'Имя:', 'Отчество:', 'Прочее (ник или лишние слова):', \
#                'Компания:', 'Тип:', 'Телефон:', 'Пол:', \
#                'Год рождения:', 'Комментарий:']

# for i in range(len(titles_list)):
#     for y in range(2):
#         if y == 0:
#             Message(width=300, text=titles_list[i]) \
#                 .grid(row=i, column=y, sticky=W)
#         else:
#             Message(width=300, text=data_personal_list[i]) \
#                 .grid(row=i, column=y)
                
# window.mainloop()

def card_output(dict_of_rows : dict , data : dict):
    window = Tk()
    window.title('Информационная карточка')
    for item in data.values():
        if type(item) == dict:
            data_new = dict(item.items())
    print(data_new)

    for i,j in dict_of_rows.items():
        for y in range(2):
            if y == 0:
                Message(width=300, text=j) \
                    .grid(row=i, column=y, sticky=W)
            else:
                Message(width=300, text=data_new[j]) \
                    .grid(row=i, column=y)
                    
    window.mainloop()
    
def colums_output(dict_of_rows : dict , data : dict):
    window = Tk()
    window.title('Информационная карточка')
    new_list =[]
    new_list_index =[]
    for i,item in data.items():
        if type(item) == dict:
            data_new = dict(item.items())
        new_list.append(data_new)
        new_list_index.append(i)
    print(new_list)
    print(new_list_index)

    Message(width=300, text="ID") \
        .grid(row=0, column=0, sticky=W)
    for i in range(len(new_list_index)):
        Message(width=300, text=new_list_index[i]) \
            .grid(row=0, column=i+1 )
    for i,j in dict_of_rows.items():
        for y in range(len(data)+1):
            if y == 0:
                Message(width=300, text=j) \
                    .grid(row=i+1, column=y, sticky=W)
            else:
                Message(width=300, text=new_list[y-1][j]) \
                    .grid(row=i+1, column=y)
    
                    
    window.mainloop()
