"""
Обчислити суму за даною формулою.
"""
from Validators import functions

functions.inform(2, 1, 'Сума')
def lab2_1_result():
    limit_of_sum = functions.input_checker("Введіть ліміт суми, пам'ятайте значення має бути невід'ємним: ", int, lambda limit_of_sum: limit_of_sum >= 0)
    value_x = functions.input_checker("Введіть значення х: ", float)
    suma = 0
    for i in range(1, limit_of_sum + 1):
        suma += i ** 2 - value_x ** 2
    print(suma)
functions.start_program(lab2_1_result)