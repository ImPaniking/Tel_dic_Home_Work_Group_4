from worck_with_base import take_from_base as TAKE
from Look_up_delete_add import look_up_by_name
from worck_with_base import row_creation_fun
from worck_with_base import rewrite_base
from Look_up_delete_add import look_up_by_name

First_name = input("\nВедите имя контакта: ")

# def GetRepearFname(tel_row)

def look_up_by_name(name , data : dict):
    return dict(filter(lambda x : x[1]["First name"] == name , data.items()))
        

Last_name = input("\nВведите фамилию: ") 

# def GetRepearLname(tel_row)

def look_up_by_name_sirname(name , sir_name, data : dict):
        return dict(filter(lambda x : x[1]["First name"] == name and x[1]["Second name"] == sir_name  , data.items()))

Other_name = input("\nВведите отчество: ")

sex = input("\nВыберете пол: ") 
for i,itme in sex_dic.items();
    print(f"{i} - > {itme}")

Type_of_Contact = input("\n")
for i,itme in type_of_contact_dic.items();
    print(f"{i} - > {itme}")

tel_number = input("\nВведите номер телефона: ")


