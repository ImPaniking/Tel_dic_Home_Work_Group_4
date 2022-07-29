# задача - получит от пользователя данные, и создать кортеж 

# |Фамилия | str| |
# |Имя | str | |
# |Отчетсво | str | |
# |Прочее ( ник или лишние слова )| str ||
# |Компания | str | |
# |тип| str ||
# |телефон| str|
# |пол | str | |
# |Год рождения| date | |
# |комментарий| str | |

from email.policy import default


def phone_number_row_creation \
    (
        First_name = "", 
        Last_name = "", 
        Other_name = "",
        Other_name_info = "", 
        Company_name = "",
        type_of_number = 1 ,
        sex = 1 ,
        bithd_day = "",
        Commentary = "" 
    ):
    row_info = [, , , , , , , , ,]
    match len(First_name.split(" ")):
            case 0:
                continue
            case 1:
                First_name = list(First_name.split(" "))[0]
            case 2:
                Last_name = list(First_name.split(" "))[1]
            case 3:
                Other_name = list(First_name.split(" "))[2]
            default:
                