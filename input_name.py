from worck_with_base import take_from_base as TAKE
from Look_up_delete_add import look_up_by_name
from worck_with_base import row_creation_fun
from worck_with_base import rewrite_base
from Look_up_delete_add import look_up_by_name

def FirstName():
    # for i,itme in tel_row.items():
    #         print(f"{i} - > {itme}")
            First_name = input("\nВедите имя контакта: ")
            data = look_up_by_name(name , TAKE())
            if len(data) < 1:
                print("нет такого пользователя")



def LastName():        
    # for i,itme in tel_row.items():
        # print(f"{i} - > {itme}")
        # print("Выберите действие: ")
        Last_name = input("\nВведите фамилию: ") 



def OtherName():
    # for i,itme in tel_row.items():
    #         print(f"{i} - > {itme}")
    #         print("Выберите действие: ")
            Other_name = input("\nВведите отчество: ")

def sex_orient(): 
    for i,itme in sex_dic.items():
        print(f"{i} - > {itme}")
        sex = input("\nВыберете пол: ")

def TypeOfContact():
    for i,itme in type_of_contact_dic.items():
        print(f"{i} - > {itme}")
        print("Выберите тип: ")
        Type_of_Contact = input("\nВыберите тип из списка: ")

def TelNumber():
    # for i,itme in tel_row.items():
    #     print(f"{i} - > {itme}
    #     print("Выберите действие: ")
        tel_number = input("\nВведите номер телефона: ")


# FirstName()
# LastName()
# sex_orient()
# TypeOfContact()
# TelNumber()
