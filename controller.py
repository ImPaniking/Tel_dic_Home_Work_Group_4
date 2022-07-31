import interface as UI
import worck_with_base as WWB
import Look_up_delete_add as LOOK
import data_output as Fancy
import dict as DIC

def one_card_or_multi(card):
    if len(card) > 1:
        Fancy.colums_output(DIC.tel_row,card)
    else :
        Fancy.card_output(DIC.tel_row,card)

def look_on_contact():
    option_value = UI.input_options_look_up ()
    match option_value:
            case 1:
                name = "Kira" # тут должен быть ввод Имени
                card = LOOK.look_up_by_name(name,WWB.take_from_base())
                one_card_or_multi(card)
            case 2:
                name = "Igor" # тут должен быть ввод Имени
                sir_name = "Penschii" # тут должен быть ввод Фамили
                card = LOOK.look_up_by_name_sirname(name,sir_name,WWB.take_from_base())
                one_card_or_multi(card)
            case 3:
                tel = "+373 68 032305" # тут должен быть ввод телефона
                card = LOOK.look_up_by_tel_number(tel,WWB.take_from_base())
                one_card_or_multi(card)
def button():
    UI.description()
    user_name = UI.say_hello()
    repeat = 2
    while repeat == 2:
        option_value = UI.input_options()
        match option_value:
            case 1:
                look_on_contact()
            case 2:
                repeat_val = True
                while repeat_val:
                        # Блок ввода информации для карточки
                    First_name = "Kira"
                    Last_name = "S"
                    Other_name = " "
                    sex_type = 2
                    contact_type = 3
                    tel_number = "+ 373 78 482305"

                    new_card = WWB.row_creation_fun\
                            (
                                    First_name = First_name, 
                                    Last_name = Last_name, 
                                    Other_name = Other_name,
                                    sex = sex_type ,
                                    type_of_contact = contact_type, 
                                    tel_number = tel_number,
                                    data = WWB.take_from_base()
                            )
                    Fancy.card_output(DIC.tel_row,new_card)
                    WWB.rewrite_base(new_card)
                    repeat_val = UI.repeat_options() 
            case 3:
                option_value = UI.options_what_to_do()
                match option_value:
                    case 1:
                        look_on_contact()
                        option_value = UI.options_find_contact()
                        match option_value:
                            case 1:
                                print("Вы его видели, когда искали =) этот пункт немного не подходит сюда, но не могу ")
                            case 2:
                                repeat_val = True
                                while repeat_val:
                                    ID_user = "6" # нужен ввод ИД человека ( то что самое первое в базе)
                                    What_to_cange = 1 # выбор из списка названий столбцов - словарик tel_row
                                    new_name = "Liza"
                                    dict_2 = WWB.take_from_base()
                                    data = LOOK.change_item_in_dict(ID_user,DIC.tel_row[What_to_cange],new_name,dict_2)
                                    WWB.rewrite_base(data)
                                    Fancy.card_output(DIC.tel_row,data)
                                    repeat_val = UI.repeat_options()
                            case 3:
                                repeat_val = True
                                while repeat_val:
                                    ID_user = input("Ввудите ID контакта для удаления") # нужен ввод ИД человека ( то что самое первое в базе)
                                    LOOK.pop_row_number(ID_user)
                                    repeat_val = UI.repeat_options()
        repeat = UI.finish_options (user_name = user_name)
button()