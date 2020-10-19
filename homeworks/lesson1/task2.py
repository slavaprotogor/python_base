"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

seconds = int(input('Введите секунды: '))

days, seconds = divmod(seconds, 24 * 60 * 60)
hours, seconds = divmod(seconds, 60 * 60)
minuts, seconds = divmod(seconds, 60)

print(f'{days:02} д. {hours:02}:{minuts:02}:{seconds:02}')
