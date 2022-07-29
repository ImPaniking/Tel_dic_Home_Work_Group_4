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
import json


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
    Перед началом загружает справочник , для того что бы подобрать последний ключ и новый добавлять по новому ключу 

    В конце - перезаписывает файл json 
    """
    with open('phone_numbers.json', 'r') as infile:
        data = json.load(infile)
    infile.close()
    phone_dic = data
    max_id = int(max(phone_dic.keys()))
    colum_dic = \
        {
            "First name" : First_name ,
            "Second name" : Last_name , 
            "Othen name" : Other_name ,
            "Type of Contact" : Dic.type_of_contact_dic[type_of_contact] , 
            "Company" : Company_name ,
            "Telefon type" : Dic.tel_type_dic[type_of_number] ,
            "Telefon number" : tel_number ,
            "E-mail" : email ,
            "Sex" : Dic.sex_dic[sex] ,
            "Birth Day" : bithd_day ,
            "Comment" : Commentary ,
            "Fav check" : fav_check
        }
    # phone_dic = {}   
    phone_dic[max_id+1] = colum_dic
    with open('phone_numbers.json', 'w') as outfile:
        json.dump(phone_dic, outfile)
    outfile.close()

phone_number_row_creation(Other_name = "Geek Study" , Company_name = "GB.ru")

