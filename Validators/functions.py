"""
Функції, що зможуть полегшити нам життя
"""
import re
def inform(lab_number: int, ex_number: int, conditions: str):
    """
    :param lab_number: номер лабораторної роботи
    :param ex_number: номер завдання
    :param conditions: умова завдання
    """
    print('Іванова Євгенія Сергіївна\nЛабораторна робота№', lab_number, '\nВаріант3\n', ex_number, ' ', conditions)

def input_checker(comment: str, types, *condition):
    """
    :param comment: коментар до вхідних даних
    :param types: тип вхідних даних
    :param condition: умова вводу
    """
    PATTERN = {str: r".+", int: r"^[-+]?[0-9]+$", float: r"[+-]?([0-9]*[.])?[0-9]+"}
    if types in PATTERN:
        while True:
            user_input = input(comment)
            if bool(re.fullmatch(PATTERN[types], user_input)):
                user_input = types(user_input)
                validat = True
                for cond in condition:
                    if callable(cond) and not cond(user_input):
                        validat = False
                        break

                if validat:
                    return types(user_input)
                else:
                    print("Невірне значення")
            else:
                print("Невірне значення, спробуйте ще раз!")
    else:
        return None

def start_program(func):
    """
    :param func: функція на запуск якої ми робимо запит
    """
    while True:
        question = str(input("Введіть yes якщо хочете запустити програму:"))
        if question == 'yes':
            func()
        else:
            raise SystemExit

