import json
import random
import hashlib
import string




def gen_salt():
    s = string.ascii_lowercase + string.digits
    return ''.join(random.sample(s, random.randint(3, 7)))


def load_data():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except:
        return {}


def save_data(data):
    with open('users.json', 'w') as file:
        json.dump(data, file, indent=2)


def hash_password(salt: str, password: str) -> str:
    passwd = salt + password
    h = hashlib.sha512(passwd.encode('utf-8')).hexdigest()
    return h


def check_password():
    passwd_to_check = input('Введите пароль: ')
    return hash_password(users[nick]['password']['salt'], passwd_to_check) == users[nick]['password']['hash']


nick = input('Введите ник для регистрации или авторизации: ')
users = load_data()
if nick in users:
    print(f'Добро пожаловать, {users[nick]["username"]}!')
    if check_password():
        print('Вход прошел успешно')
    else:
        for i in range(0, 3):
            print(f'неверный пароль. У вас осталось {3-i} попыток')
            if check_password():
                break
        print('Вы потратили все попытки ввода пароля. Попробуйте повторить вход через 50 лет')

else:
    password = input('Ваша учетная запись отсутствует в базе. Введите пароль для новой учетной записи: ')
    salt = gen_salt()
    user = {nick: {'username': nick, 'password': {'hash': hash_password(password, salt), 'salt': salt}}}
    save_data(user)

