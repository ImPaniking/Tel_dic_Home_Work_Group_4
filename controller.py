import interface as UI
import worck_with_base as WWB
import Look_up_delete_add as LOOK
import data_output as Fancy
import dict as DIC


UI.description()

user_name = UI.say_hello()
option_value = UI.input_options()
match option_value:
    case 1:
        option_value = UI.input_options_look_up ()
        match option_value:
            case 1:
                name = "Artion"
                card = LOOK.look_up_by_name(name,WWB.take_from_base())
                print(card)
                Fancy.card_output(DIC.tel_row,card)
            case 2:
                name = "Igor"
                sir_name = "Penschii"
                card = LOOK.look_up_by_name_sirname(name,sir_name,WWB.take_from_base())
                Fancy.card_output(DIC.tel_row,card)
            case 3:
                tel = "+373 68 032305"
                card = LOOK.look_up_by_tel_number(tel,WWB.take_from_base())
                Fancy.card_output(DIC.tel_row,card)
    case 2:
        WWB.row_creation_fun()
    case 3:
        print("ERROR 404 , WORCK IN PRGRESS")
