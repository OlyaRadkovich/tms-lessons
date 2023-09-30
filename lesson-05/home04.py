# 4. Напишите функцию get_longest_word, которая на вход
# принимает текст (только английские слова и пробелы), и
# возвращает самое длинное слово из этого текста. Для
# разбиения строки на слова используйте функцию split.

def get_longest_word(input_text):
    words = input_text.split()
    longest = max(words, key=len)
    return f'The longest word in this text: {longest}'


assert get_longest_word('What generative networks can do') == 'The longest word in this text: generative'
