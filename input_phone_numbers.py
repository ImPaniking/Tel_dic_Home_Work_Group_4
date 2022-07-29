# задача - получит от пользователя данные, и создать кортеж 

# |Фамилия | str| |
# |Имя | str | |
# |Отчетсво | str | |
# |Прочее ( ник или лишние слова )| str ||
# |Компания | str | |
# |тип| str ||
# |телефон| str|
# |пол | str | |
# |Год рождения| date | |
# |комментарий| str | |

import dictionarys as Dic


def phone_number_row_creation \
    (
        First_name = " ", 
        Last_name = " ", 
        Other_name = " ",
        type_of_contact = 0, 
        Company_name = " ",
        type_of_number = 0 ,
        tel_number = " ",
        email = " ",
        sex = 0 ,
        bithd_day = " ",
        Commentary = " " ,
        fav_check = False
    ):
    """Метод - принимает на вход параметры телефонного справочника, если они не заданы - использует значения по умолчанию

    Returns:
        str: на выходе строка , полей с разделителем '|'
    """

    ID_number = 1
    colum_dic = \
        {
            0 : ID_number ,
            1 : First_name ,
            2 : Last_name , 
            3 : Other_name ,
            4 : Dic.type_of_contact_dic[type_of_contact] , 
            5 : Company_name ,
            6 : Dic.tel_type_dic[type_of_number] ,
            7 : email ,
            8 : tel_number ,
            9 : Dic.sex_dic[sex] ,
            10 : bithd_day ,
            11 : Commentary ,
            12 : fav_check
        }
    return '|'.join(map(str , colum_dic.values()))


print(phone_number_row_creation())


