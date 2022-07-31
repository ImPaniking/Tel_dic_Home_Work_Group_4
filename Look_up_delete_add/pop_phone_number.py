# Код удаления строчки из записной книжки

from worck_with_base import rewrite_base
from worck_with_base import take_from_base

def pop_row_number(ID_number : str):
    phone_dic = take_from_base()
    phone_dic.pop(ID_number)
    rewrite_base(phone_dic)
    