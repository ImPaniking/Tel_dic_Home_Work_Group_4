from worck_with_base import take_from_base as TAKE
from Look_up_delete_add import look_up_by_name

phone_dic = TAKE()

for i in phone_dic.keys():
    print(phone_dic[i]["First name"])
print(look_up_by_name("Артём",TAKE()))