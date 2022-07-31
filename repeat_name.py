# проверка ввода на повтор имени и фамилии
# на повторение 


import dictionarys
import json

def look_up_by_name(name , data : dict):
    return dict(filter(lambda x : x[1]["First name"] == name , data.items()))
        for x[1] == name 
        return name

def look_up_by_name_sirname(name , sir_name, data : dict):
        return dict(filter(lambda x : x[1]["First name"] == name and x[1]["Second name"] == sir_name  , data.items()))
        if First_name == name





#-----------------------------------------------------------------------------------
#поиск по json
# new_dict = dict(filter(lambda x : x[1]["First name"] == name , data.items())) # коротко ф-я ниже
# def look_up_by_name(name , data : dict):
#     new_dict = {}
#     for x,y in data.items():
#         if y["First name"] == name:
#             new_dict[x] = y
#     print(new_dict)

# перевод списка из json в python

# import dictionarys<font></font>
# import json<font></font>
# f = open(os.environ["HOME"] + "/list_name.json", "r", encoding="utf-8")<font></font>
# data = json.load(f)<font></font>
# f.close()<font></font>

# получение коднейм правда не понимаю для чего?
# for _name in data["names"]: <font></font>
#     print(_name["codename"])<font></font>

#     for _last_name in _name["last_names"]: <font></font>
#         print("  " + _last_name)<font></font>


#------------------------------------------------------------------------------------------

# def __init__(self):
#     self.last_name = last_name
#     self.name = name


# def __str__(self):
#     return 'Member("{}", "{}")'.format(self.last_name, self.name)

# class Contacts:
#     def find_member(self, query):
#         with open('data.txt') as file:
#             for line in file:
#                 member = Member(from_line=line)
#                 if (member.last_name, member.name) == query:
#                     return member

# def add_member(self):
#     m = Member()
#     m.input_characters()
#     if c.find_member(query=(m.last_name, m.name)) is None:
#         f = open('data.txt', 'a')
#         f.write('{0:10} | {1:10} | {2}'.format(m.last_name, m.name) + '\n')
#         print('\nКонтакт {lastName} {name} успешно добавлен\n'.format(lastName=m.last_name, name=m.name))
#         f.close()
#     else:
#         print('Такой контакт уже есть')

# -------------------------------------------------------------------------------

# проверки

# def correct_name(text):
#     name = input(f'{text} ')
#     while not all(map(str.isalpha,name)):
#         print('не корректный ввод')
#         name = input(f'{text} ')
#     return name.capitalize()

# name = correct_name('имя')
# surname = correct_name('фамилия')

# def correct_name(text):
#     name = input(f'{text} ')
#     while True:
#         if name.isalpha():
#             return name.capitalize()
#         print('не корректный ввод')
#         name = input(f'{text} ')


# def readfile(filename):
#     # чтение файла при запуске
#     return open(filename).read().split('\n')

# def scan(data):
#     # Просмотр всех записей справочника:
#     for i in  data:
#         print(i)
        
def search(data):
    # Поиск по справочнику.
    flag = 1
    name = input('имя > ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('Имя не найдено')
