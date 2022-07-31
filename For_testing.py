from worck_with_base import take_from_base as TAKE
from Look_up_delete_add import pop_row_number 
from worck_with_base import rewrite_base

phone_dic = TAKE()

for i in phone_dic.keys():
    print(phone_dic[i]["First name"])

pop_row_number('2')