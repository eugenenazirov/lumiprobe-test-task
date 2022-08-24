'''3. Напишите функцию, которая принимает на вход строку,
состояющую из символов '(' и ')', задающих скобочную последовательность,
и возвращает True, если последовательность корректна, иначе False.'''


def check_brackets(brackets_str: str):
    opened_brackets = 0
    brackets_list = list(brackets_str)
    if brackets_list[0] == ")" or brackets_list[-1] == "(":
        return False
    for bracket in brackets_list:
        if bracket == "(":
            opened_brackets += 1
        elif bracket == ")":
            opened_brackets -= 1
        else:
            return False
    return opened_brackets == 0


print(check_brackets("(()(()())()))"))
print(check_brackets("((()))"))
