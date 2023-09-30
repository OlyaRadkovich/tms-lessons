# * Напишите функцию get_most_frequent_word, которая на вход
# принимает текст (только английские слова и пробелы), и
# возвращает самое часто встречающееся слово. Если таких
# слов несколько - верните любое.

def get_most_frequent_word(sentence):
    words = sentence.split()
    frequent_word = max(words, key=words.count)
    return frequent_word


assert get_most_frequent_word('How many times can you repeat the same same same thing?') == 'same'
