"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""

distance = int(input('Введите дистанцию первого дня (км.): '))
distance_target = int(input('Введите целевую дистанцию (км.): '))

day = 1
while distance < distance_target:
    day += 1
    distance *= 1.1
    print(f'{day}-й день: {distance:.2f} км.')

print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {distance:.2f} км.')
