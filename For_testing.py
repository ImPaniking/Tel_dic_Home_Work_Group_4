from worck_with_base import take_from_base as TAKE
from Look_up_delete_add import look_up_by_name
from worck_with_base import row_creation_fun
from worck_with_base import rewrite_base
from Look_up_delete_add import look_up_by_name
from Look_up_delete_add import change_item_in_dict
from data_output import colums_output
from data_output import card_output
from dict import tel_row

phone_dic = TAKE()

# for i in phone_dic.keys():
#     print(phone_dic[i]["First name"])
# print(look_up_by_name("Artiom",TAKE()))

rewrite_base\
    (row_creation_fun\
    (
        First_name = "Liza", 
        Last_name = "S", 
        Other_name = " ",
        sex = 2 ,
        type_of_contact = 1, 
        tel_number = "+ 373 78 482305",
        data = TAKE()
        
    ))

# rewrite_base\
#     (change_item_in_dict\
#         ('1',
#         "First name", 
#         "Artiom", 
#         TAKE()
#         )
#     )

# colums_output(tel_row,TAKE())


# for i,itme in tel_row.items():
#     print(f"{i} - > {itme}")

# print(tel_row)