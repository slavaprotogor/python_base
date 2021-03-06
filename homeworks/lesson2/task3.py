"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

mounth_mapper = [
    'зима', 'зима', 'весна', 'весна',
    'весна', 'лето', 'лето', 'лето',
    'осень', 'осень', 'осень', 'зима'
]

while True:
    mounth = input('Введите месяц (целое число): ')

    if not mounth.isdigit():
        print('Должно быть введено целое число. Попробуйте еще раз.')
        continue

    mounth = int(mounth)
    if mounth > 12:
        print('Месяцев не может быть больше 12. Попробуйте еще раз.')
        continue

    if mounth < 1:
        print('Месяцев не может быть меньше 1. Попробуйте еще раз.')
        continue

    break

print(f'{mounth} месяц - {mounth_mapper[mounth - 1]}')
