"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

digits = []
while True:
    digit = input('Введите число (q - выход): ')

    if digit == 'q':
        break

    if not digit.isdigit():
        print('Должно быть введино целое число. Попробуйте еще раз.')
        continue

    digit = int(digit)
    for index, digit_item in enumerate(digits):
        if digit > digit_item:
            digits.insert(index, digit)
            break
    else:
        digits.append(digit)

print('Неубывающая последовательность: ', digits)
