from database.crud import login_patient, login_professional, register_patient, status_update, create_professional, history_triagem, make_triagem, set_temperature, cancel_triagem, seach_patient
from menus import options_menu, login_options, menu_patient, menu_professional

from sys import exit

while True:
    options = options_menu(3)
    if options == 1:
        while True:
            login = login_options()
            if login == 1:
                login_id = login_patient()
                if login_id:
                    while True:
                        option = menu_patient()

                        if option == 1:
                            make_triagem(login_id)

                        elif option == 2:
                            history_triagem(login_id)

                        elif option == 3:
                            cancel_triagem(login_id)

                        elif option == 0:
                            exit()

            elif login == 2:
                loged = login_professional()

                if loged:
                    patient = seach_patient()
                    while True:
                        option = menu_professional()
                        if option == 1:
                            set_temperature(patient)

                        elif option == 2:
                            status_update(patient)

                        elif option == 3:
                            history_triagem(patient)

                        elif option == 0:
                            break
                        else:
                            print("erro")
            elif login == 0:
                break
    elif options == 2:
        register_patient()

    elif options == 3:
        create_professional()

    elif options == 0:
        break




