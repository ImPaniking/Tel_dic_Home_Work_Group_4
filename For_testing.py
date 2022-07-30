import json
from dic_of_numbers_creation import phone_number_row_creation


with open('phone_numbers.json', 'r') as infile:
        data = json.load(infile)
        infile.close()
phone_dic = data

for i in phone_dic.keys():
    print(phone_dic[i]["First name"])

# phone_number_row_creation \
#     (
#         First_name = "Люда", 
#         Last_name = "", 
#         Other_name = "",
#         type_of_contact = 2, 
#         sex = 2 ,
#         bithd_day = "24/02/1989",
#         Commentary = "Подргуга" ,
#         Company_name = "",
#         fav_check = True ,
#         type_of_number = 3 ,
#         tel_number = " +373 79 999999 ",
#         telefon_comment = "" ,
#         email = "",
        
#     )
