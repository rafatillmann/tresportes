import re
import string
import random


characters = list(string.ascii_letters + string.digits)


def generate_random_password():

    random.shuffle(characters)

    password = []
    for i in range(10):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)


def cpf_validate(numbers):
    cpf = [int(char) for char in numbers if char.isdigit()]

    if len(cpf) != 11:
        return False
    if cpf == cpf[::-1]:
        return False

    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def email_validate(email):

    if(re.search(regex, email)):
        return True
    else:
        return False
