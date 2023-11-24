def validate_options(number):
    option = input()
    try:
        option = int(option)
        if option > number:
            raise ValueError
        return option
    except ValueError:
        print("Digite uma opção valida")
        return None


def validate_information(name):
    while True:
        try:
            value = input(f"Digite seu {name}: ").replace(" ", "").replace(".", "").replace("-", "")
            if len(value) == 11:
                value = int(value)
                return value
            else:
                raise ValueError
        except (AttributeError, ValueError):
            print(f"Digite o {name.split()[0]} corretamente")


def password_confirm():
    while True:
        password = input("Digite sua senha: ")
        if " " in password:
            print("Senha não pode conter 'Espaço'!")
        else:
            confirm_password = input("Confirme sua senha: ")
            if password == confirm_password:
                return password
            else:
                print("Senhas não correspondem ")


def validate_triagem(question):
    while True:
        print(question)
        print("(1) Sim")
        print("(2) Não")
        option = validate_options(2)
        if option:
            return option