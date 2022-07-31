# Код удаления строчки из записной книжки
import json
from worck_with_base import rewrite_base as RE
from worck_with_base import take_from_base as TAKE

def pop_row_number(ID_number : str):
    phone_dic = TAKE()
    phone_dic.pop(ID_number)
    RE()
    