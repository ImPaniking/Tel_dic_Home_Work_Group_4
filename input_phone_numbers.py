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
        sex = 0 ,
        bithd_day = " ",
        Commentary = " " ,
        Company_name = " ",
        fav_check = False ,
        type_of_number = 0 ,
        tel_number = " ",
        telefon_comment = "" ,
        email = " ",
        
    ):
    """Метод - принимает на вход параметры телефонного справочника, если они не заданы - использует значения по умолчанию
    Перед началом загружает справочник , для того что бы подобрать последний ключ и новый добавлять по новому ключу 

    В конце - перезаписывает файл json 
    """
    with open('phone_numbers.json', 'r') as infile:
        data = json.load(infile)
    infile.close()
    phone_dic = data
    tel_number_dic = \
        {
            "Telefon type" : Dic.tel_type_dic[type_of_number] ,
            "Telefon number" : tel_number ,
            "Telefon comment" : telefon_comment,
            "E-mail" : email  
        } 
    person_info = \
        {
            "First name" : First_name ,
            "Second name" : Last_name , 
            "Othen name" : Other_name ,
            "Type of Contact" : Dic.type_of_contact_dic[type_of_contact] , 
            "Sex" : Dic.sex_dic[sex] ,
            "Birth Day" : bithd_day ,
            "Comment" : Commentary ,
            "Company" : Company_name ,
            "Fav check" : fav_check,
            "Tel_info" : tel_number_dic
        }
    phone_dic[int(max(phone_dic.keys()))+1] = person_info
    with open('phone_numbers.json', 'w') as outfile:
        json.dump(phone_dic, outfile)
    outfile.close()

phone_number_row_creation \
    (
        First_name = "Артём", 
        Last_name = "Пенский", 
        Other_name = "ImPanikin",
        type_of_contact = 3, 
        sex = 1 ,
        bithd_day = "07/03/1991",
        Commentary = "Личные данные" ,
        Company_name = "ICS Vistarcom SRL",
        fav_check = True ,
        type_of_number = 3 ,
        tel_number = " +373 68 032305 ",
        telefon_comment = "" ,
        email = "artiom.penschii91@gmail.com",
        
    )

