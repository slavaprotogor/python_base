"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
from helpers import input_type


def user_info(name: str, surname: str, year: int, city: str, email: str, phone: str):
    print(f'Имя: {name}, фамилия:  {surname}, год рождения: {year},'
          f' город проживания: {city}, электронная почта: {email}, телефон: {phone}')


name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
year = input_type('Ваш год рождения: ', check_type=int)
city = input('Ваш город проживания: ')
email = input('Ваш email: ')
phone = input('Ваш телефон: ')

user_info(name=name, surname=surname, year=year, city=city, email=email, phone=phone)
