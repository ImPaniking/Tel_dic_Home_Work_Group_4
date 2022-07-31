# модуль поиска карточки

def look_up_by_name(name , data : dict):
    return dict(filter(lambda x : x[1]["First name"] == name , data.items()))

def look_up_by_name_sirname(name , sir_name, data : dict):
        return dict(filter(lambda x : x[1]["First name"] == name and x[1]["Second name"] == sir_name  , data.items()))

def look_up_by_tel_number(tel_number, data : dict):
        return dict(filter(lambda x : x[1]["Tel number"]==  tel_number, data.items()))

def look_up_by_sex(sex, data : dict):
        return dict(filter(lambda x : x[1]["Sex"]==  sex, data.items()))

def look_up_by_type_of_contact(type_of_contac, data : dict):
        return dict(filter(lambda x : x[1]["Type of contact"]==  type_of_contac, data.items()))



