"""
Обчислення конкретної функції, в залежності від введеного значення х
"""
from Validators import functions

functions.inform(1, 3, "Обчислення функції")
def lab1_3_result():
    x = functions.input_checker("Введіть значення х: ", float)
    if x <= -3:
        f = 9
    else:
        f = 1 / (x ** 2 + 1)
    print("F(x)=", f)
functions.start_program(lab1_3_result)