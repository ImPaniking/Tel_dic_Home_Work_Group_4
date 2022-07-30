import json
with open('phone_numbers.json', 'r') as infile:
        data = json.load(infile)
        infile.close()
phone_dic = data

for i in phone_dic.keys():
    print(phone_dic[i]["First name"])