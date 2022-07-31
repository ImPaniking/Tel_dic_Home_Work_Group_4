from methods import check_value_is_digit_and_return_it as check

# Вступление: краткое описание программы
def description ():
    print ('\nДанный телефонный справочник позволяет добавлять, просматривать, редактировать и удалять контакты, \
                    \nа также импортировать и экспортировать данные.')

# Спрашиваем имя пользователя и Приветствуем пользователя
def say_hello ():
    user_name = input('\nПредставьтесь, пожалуйста. Напишите ваше имя: ')
    print(f'\nЗдравствуйте, {user_name}!')
    return user_name

# Выбираем опцию: Найти контакт,  Добавить новый контакт или Работа с данными
def input_options ( opt_inquiry = '\nКакую операцию собираетесь произвести? Найти контакт [1],  Добавить [2] или Работа с данными [3]: ',
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

# Выбор как искать контакт
def input_options_look_up ( opt_inquiry = '\nПо какому полю будет искать контакт? Имя [1],  Имя + Фамилия [2] Телефон [3]: ',
                    opt_1 = 'Поиск контакта по Имени.\n',
                    opt_2 = 'Поиск контакта по Имени + Фамилии.\n',
                    opt_3 = 'Поиск контакта по телефону.\n'):
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

# Выбираем опцию, когда нашли контакт: Добавить новый контакт или Работа с данными
def options_find_contact ( opt_inquiry = 'Запись контакта найдена. Что будем с ней делать? Просмотреть [1],  Редактировать [2] или Удалить [3]: ',
                                opt_1 = 'Посмотреть информацию о контакте.\n',
                                opt_2 = 'Внести изменения в запись контакта.\n',
                                opt_3 = 'Удалить контакт.\n'):
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

def options_what_to_do ( opt_inquiry = 'Какая работа с базой нужна? Работа с контактом(Смотреть/Редактировать/Удалить) [1],  Импорт/Экспорт базы [2] или ??? [3]: ',
                                opt_1 = 'Выберите контакт для работы с ним.\n',
                                opt_2 = 'Импорт/Экспорт базы(Пока не готово =( )).\n',
                                opt_3 = 'ERROR 404.\n'):
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

# Выбираем опцию, когда перешли в Работу с данными: Экспорт или Импорт
def options_data_work ( opt_inquiry = 'Требуется произвести Экспорт [1] или Импорт [2] данных: ',
                        opt_1 = 'Экспортирование даных.\n',
                        opt_2 = 'Импортирование данных.\n'):
    count = 0
    while count < 3:
        option_value = check(opt_inquiry)
        if option_value == 1:
            print (opt_1)
            break
        elif option_value == 2:
            print (opt_2)
            break
        else:
            print(f'Неверный ввод. У вас осталось {2-count} попыток ввода')
            count +=1
    return option_value

# Спрашиваем о завершении работы программы или о новом действии. Если выбрано Завершение, в дальнейшем следует завершить
# программу.
def finish_options (opt_inquiry = 'Вы закончили работу со справочником? Да, завершить работу [1] или Нет, я хочу поработать еще [2]: ',
                        opt_1 = 'Завершение работы. Выход из программы.\n',
                        opt_2 = 'Продолжаем работу.\n'):
    count = 0
    while count < 3:
        option_value = check(opt_inquiry)
        if option_value == 1:
            print (opt_1)
            say_bye (user_name)
            break
        elif option_value == 2:
            input_options()
            break
        else:
            print(f'Неверный ввод. У вас осталось {2-count} попыток ввода')
            count +=1
    return option_value
# затычка - коротинкая проверка на повтор =)
def repeat_options ():
    result = print("Повторить ? y - > да / n - > нет")
    if result == "n":
        return False
    else :
        return True

# Прощаемся с пользователем
def say_bye (user_name):
    return print(f'Всего хорошего и до скорых встреч, {user_name}!')

# description ()
# user_name = say_hello()
# input_options()
# options_find_contact()
# options_data_work()
# finish_options()
# say_bye(user_name)