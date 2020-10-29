"""
Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
from helpers import my_map, my_capitalize, is_latin_lower


while True:
    word = input('Введите слово: ')
    if not is_latin_lower(word):
        print('Текст содержит не только латинские буквы в нижнем регистре. '
              'Поробуйте снова.')
        continue

    word_capitalize = my_capitalize(word)
    print('Результат: ', word_capitalize)

    if input('Прервать ввод? (y/n): ').lower() == 'y':
        break

while True:
    text = input('Введите предложение: ')
    words = text.split()
    if not is_latin_lower(''.join(words)):
        print('Текст содержит не только латинские буквы в нижнем регистре. '
              'Поробуйте снова.')
        continue

    text_capitalized = ' '.join(my_map(my_capitalize, words))
    print('Результат: ', text_capitalized)

    if input('Прервать ввод? (y/n): ').lower() == 'y':
        break
