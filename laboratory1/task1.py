"""
Катети прямокутного трикутника уводяться з клавіатури.
Обчислити довжину гіпотенузи, периметр і площу цього трикутника.
Відповідь дати з точністю до 10 знаків після коми.
"""
from Validators import functions

functions.inform(1, 1, "Обчислення гіпотенузи, периметра і площі трикутника")
def lab1_1_result():
    katet1 = functions.input_checker("Введіть довжину катета 1: ", float, lambda katet1: katet1 > 0)
    katet2 = functions.input_checker("Введіть довжину катета 2: ", float, lambda katet2: katet2 > 0)
    gipotenusa = (katet1 ** 2 + katet2 ** 2) ** (1 / 2)
    perimetr = katet1+katet2+gipotenusa
    plosha = (katet1*katet2)/2
    print("Гіпотенуза: "'%.10f' %gipotenusa +"\nПериметр: "'%.10f' %perimetr + "\nПлоща: "'%.10f' %plosha)
functions.start_program(lab1_1_result)


