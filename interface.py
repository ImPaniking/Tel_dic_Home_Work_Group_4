from methods import check_value_is_digit_and_return_it as check

# Вступление: краткое описание программы
def description ():
    return print ('\nДанный телефонный справочник позволяет добавлять, просматривать, редактировать и удалять контакты, \
                    \nа также импортировать и экспортировать данные.')

# Спрашиваем имя пользователя и приветствуем его
def say_hello ():
    user_name = input('\nПредставьтесь, пожалуйста. Напишите ваше имя: ')
    print(f'Здравствуйте, {user_name}!')

# Выбираем опцию
def input_options ( opt_inquiry = 'Какую операцию собираетесь произвести? Найти контакт [1],  Добавить [2] или Работа с данными [3]: ',
                    opt_1 = 'Поиск контакта для просмотра и редактирования.\n',
                    opt_2 = 'Добавление нового контакта.\n',
                    opt_3 = 'Работа с данными.\n'):
    count = 0
    while count < 3:
        option_value = check(opt_inquiry)
        if option_value == 1:
            print (opt_1)
            break
        elif option_value == 2:
            print (opt_2)
            break
        elif option_value == 3:
            print (opt_3)
            break
        else:
            print(f'Неверный ввод. У вас осталось {2-count} попыток ввода')
            count +=1
    return option_value

description()
say_hello()
input_options()