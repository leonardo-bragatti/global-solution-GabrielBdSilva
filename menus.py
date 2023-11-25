from functions import validate_options


def options_menu(number):
    print("-" * 8, "Menu", "-" * 8)
    print("(1) Login Paciente/Profissional")
    print("(2) Cadastrar Paciente")
    print("(3) Cadastrar profissional(Para o hospital)")
    print("(0) Sair")
    option = validate_options(number)
    return option


def login_options():
    while True:
        print("-" * 5, "Fazer login como", "-" * 5)
        print("(1) Paciente")
        print("(2) Profissional")
        print("(0) Voltar")
        option = validate_options(2)
        if option is not None:
            return option
        else:
            pass


def menu_patient():
    while True:
        print("-" * 8, "Menu Paciente", "-" * 8)
        print("(1) Fazer triagem online")
        print("(2) Ver historico de triagens")
        print("(3) Cancelar Consulta")
        print("(0) Sair")
        option = validate_options(3)
        if option is not None:
            return option
        else:
            pass


def menu_professional():
    while True:
        print("-" * 8, "Menu Profissional", "-" * 8)
        print("(1) Adicionar pressão e temperatura a triagem")
        print("(2) atualizar status da triagem")
        print("(3) Ver historico de triagems")
        print("(0) Voltar")
        option = validate_options(3)
        if option is not None:
            return option
        else:
            pass


def show_triagem_confirm(symptoms, pain_level, taking_medication, breathing, fever):
    print("-"*20)
    print(f"Sintomas: {symptoms}")
    print(f"Nivel de dor: {pain_level}")
    print(f"Tomando algum medicamento: {taking_medication}")
    print(f"Dificuldade respiratoria: {breathing}")
    print(f"Teve febre em 48h: {fever}")


def show_triagems(triagem):
    print("-"*10)
    print(f"ID: {triagem.id}")
    print(f"Status: {triagem.status}")
    print(f"Symptoms: {triagem.symptoms}")
    print(f"Pain_level: {triagem.pain_level}")
    print(f"Taking_medication: {triagem.taking_medication}")
    print(f"Breathing: {triagem.breathing}")
    print(f"Fever: {triagem.fever}")
    print(f"Temperature: {triagem.temperature}")
    print(f"Pressure: {triagem.pressure}")
