import random
import string
from faker import Faker

fake = Faker()


def generate_login():
    """С целью снижения коллизий с уже заведёнными курьерами - логин генерируем как рандомный набор букв"""
    return "".join(random.choice(string.ascii_lowercase) for _ in range(16))


def generate_password():
    return fake.password(length=8, digits=True)


def generate_firstname():
    return fake.first_name()
