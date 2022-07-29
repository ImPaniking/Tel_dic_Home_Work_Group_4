# Код удаления строчки из записной книжки

import json

def pop_row_number(ID_number : str):
    with open('phone_numbers.json', 'r') as infile:
        data = json.load(infile)
    infile.close()
    phone_dic = data
    phone_dic.pop(ID_number)
    with open('phone_numbers.json', 'w') as outfile:
        json.dump(phone_dic, outfile)
    outfile.close()
    
pop_row_number('1')