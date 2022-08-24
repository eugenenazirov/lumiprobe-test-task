'''1. Напишите функцию, которая на вход принимает строку, 
состоящую из строчных и заглавных латинских символов, 
а возвращает кортеж из двух элементов:
символа, который встречается в строке чаще всего (без учета регистра!),
и числа вхождений этого символа в строку.
Если таких символов несколько, функция должна вернуть любой из них.
Например, для строки "aaaAAAbc" результатом работы функции будет ('a', 6).'''


def count_letters(letters: str):
    list_of_letters = list(letters.lower())
    count = {}
    for l in list_of_letters:
        pair = {l: list_of_letters.count(l)}
        if l not in count:
            count.update(pair)
        max_letter, max_count = l, pair[l]
    for k, v in count.items():
        if v > max_count:
            max_letter, max_count = k, v
    return max_letter, max_count


print(count_letters("aaaAAAbcdddeeeefffghhhhhiigkkk"))
