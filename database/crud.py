from database.models import Triagem, Profissional, Usuario
from database import SessionLocal

from functions import validate_information, password_confirm, validate_options, validate_triagem
from menus import show_triagems, show_triagem_confirm


def register_patient():
    print("-" * 5 + "Cadastro do Paciente" + "-" * 5)
    name = input("Digite seu nome completo: ").title()
    password = password_confirm()
    email = input("Digite seu email: ")
    cpf = "CPF"
    cpf = validate_information(cpf)
    phone = "telefone (+55) "
    phone = validate_information(phone)
    birth = input("Digite sua data de nascimento dia/mes/ano: ")
    db = SessionLocal()
    try:
        users = Usuario()
        users.name = name
        users.password = password
        users.email = email
        users.cpf = cpf
        users.phone = phone
        users.birth = birth
        db.add(users)
        db.commit()
    finally:
        db.close()
    print(f"Paciente {name}, cadastrado com sucesso!")


def validate_login(user):
    if user:
        senha_digitada = input("Digite sua senha: ")
        if user.password == senha_digitada:
            print("Logado com sucesso!")
            return user.id
        else:
            print("Senha incorreta!")
    else:
        print("Não registrado!")


def login_patient():
    while True:
        print("-" * 5 + "Login Paciente" + "-" * 5)
        try:
            patient = int(input("CPF do paciente: "))
            user = get_patient(patient)
            login = validate_login(user)
            return login
        except (AttributeError, ValueError):
            print("CPF Inválido")


def login_professional():
    print("-" * 5 + "Login Profissonal" + "-" * 5)
    professional = input("Usuário de profissional: ")
    user = get_professional(professional)
    login = validate_login(user)
    return login


def create_professional():
    usuario = input("user: ")
    password = input("password: ")
    db = SessionLocal()
    try:
        user = Profissional()
        user.usuario = usuario
        user.password = password
        db.add(user)
        db.commit()
        print("Profissional cadastrado!")
    finally:
        db.close()


def make_triagem(login_id):
    print("-" * 8 + "Triagem" + "-" * 8)
    symptoms = input("Quais sintomas está sentindo? ").title()
    while True:
        print("Nivel de dor 1 a 10 (sendo 1 a mais fraca e 10 a mais forte)? ")
        pain_level = validate_options(10)
        if pain_level:
            break
        elif pain_level is None:
            pass

    question = ("Está tomando algum medicamento?")
    taking_medication = validate_triagem(question)
    if taking_medication == 1:
        taking_medication = input("Qual medicamento está tomando? ").title()
    elif taking_medication == 2:
        taking_medication = "Não"

    question = ("Dificuldade de respiração?")
    breathing = validate_triagem(question)
    if breathing == 1:
        breathing = "Dificuldade"
    elif breathing == 2:
        breathing = "Normal"

    question = ("Sentiu febre nas ultimas 48 horas?")
    fever = validate_triagem(question)
    if fever == 1:
        fever = "Sim"
    elif fever == 2:
        fever = "Não"
    show_triagem_confirm(symptoms, pain_level, taking_medication, breathing, fever)
    db = SessionLocal()
    try:
        triagem = Triagem()
        triagem.status = "Pendente"
        triagem.symptoms = symptoms
        triagem.pain_level = pain_level
        triagem.taking_medication = taking_medication
        triagem.breathing = breathing
        triagem.fever = fever
        triagem.user_id = login_id
        db.add(triagem)
        db.commit()
    finally:
        db.close()
    print(f"Triagem realizada com sucesso, você tem 48h comparecer a um estabelecimento nosso")


def history_triagem(login_id):
    triagems = get_triagem()
    for triagem in triagems:
        if triagem.user_id == login_id:
            show_triagems(triagem)
            return triagem


def history_triagens_pending(login_id):
    triagems = get_triagem()
    for triagem in triagems:
        if triagem.user_id == login_id:
            if triagem.status == "Pendente":
                show_triagems(triagem)
                return triagem


def seach_patient():
    while True:
        try:
            print("-" * 20)
            cpf = int(input("CPF do paciente que deseja abrir o menu: "))
            patient = get_patient(cpf)
            patient = patient.id
            return patient
        except (AttributeError, ValueError):
            print("CPF Inválido")


def cancel_triagem(login_id):
    triagems_pending = history_triagens_pending(login_id)
    if triagems_pending is None:
        print("Nenhuma triagem para cancelar!")
    else:
        id_triagem = input("Digite o ID da triagem que deseja cancelar: ")
        del_triagem(id_triagem)


def set_temperature(patient):
    triagems_pending = history_triagens_pending(patient)
    if triagems_pending is None:
        print("Nenhuma triagem pendente!")
    else:
        id_triagem = input("Digite o ID da triagem que deseja: ")
        triagem_user = get_triagem_id(id_triagem)
        temperature = input("Temperatura do paciente: ")
        pressure = input("Pressão do paciente:")

        db = SessionLocal()
        try:
            triagem_user.temperature = temperature
            triagem_user.pressure = pressure
            db.add(triagem_user)
            db.commit()
            print("Temperatura e pressão alterados com sucesso!")
        finally:
            db.close()


def status_update(patient):
    triagems_pending = history_triagens_pending(patient)
    if triagems_pending is None:
        print("Nenhuma triagem pendente!")
    else:
        id_triagem = input("Digite o ID da triagem que deseja: ")
        triagem_user = get_triagem_id(id_triagem)
        question = ("Deseja finalizar essa triagem? ")
        status = validate_triagem(question)
        if status == 1:
            status = "Finalizado"
            print("Status da triagem alterado com sucesso!")
        elif status == 2:
            status = "Pendente"
        db = SessionLocal()
        try:
            triagem_user.status = status
            db.add(triagem_user)
            db.commit()
        finally:
            db.close()


def get_triagem_user(user):
    db = SessionLocal()
    try:
        patient = db.query(Triagem).filter(Triagem.user_id == user).first()
        return patient
    finally:
        db.close()


def get_triagem_id(triagem_id):
    db = SessionLocal()
    try:
        triagem = db.query(Triagem).filter(Triagem.id == triagem_id).first()
        return triagem
    finally:
        db.close()


def get_patient(cpf):
    db = SessionLocal()
    try:
        patient = db.query(Usuario).filter(Usuario.cpf == cpf).first()
        return patient
    finally:
        db.close()


def get_professional(user):
    db = SessionLocal()
    try:
        user = db.query(Profissional).filter(Profissional.usuario == user).first()
        return user
    finally:
        db.close()


def del_triagem(triagem_id):
    db = SessionLocal()
    try:
        triagem_id = db.query(Triagem).filter(Triagem.id == triagem_id).first()
        db.delete(triagem_id)
        db.commit()
        print("Triagem Cancelada com sucesso!")
        return triagem_id
    finally:
        db.close()


def get_users():
    db = SessionLocal()
    try:
        users = db.query(Usuario)
        return users
    finally:
        db.close()


def get_triagem():
    db = SessionLocal()
    try:
        triagems = db.query(Triagem)
        return triagems
    finally:
        db.close()
