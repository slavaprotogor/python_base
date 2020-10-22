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
from helpers import my_map, my_capitalize


word = input('Введите слово: ')
word_capitalize = my_capitalize(word)
print('Результат: ', word_capitalize)

text = input('Введите предложение: ')
words = text.split()
text_capitalized = ' '.join(my_map(my_capitalize, words))
print('Результат: ', text_capitalized)
