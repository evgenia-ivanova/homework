"""
Організувати безперервне введення чисел з клавіатури, поки користувач не введе 0.
Після введення нуля, показати на екрані кількість чисел, які були введені,їх загальну суму і середнє арифметичне.
"""
from Validators import functions

functions.inform(2, 2, "Організувати безперервне введення чисел з клавіатури, поки користувач не введе 0."
                       "\n Після введення нуля, показати на екрані кількість чисел, які були введені,"
                       "\n їх загальну суму і середнє арифметичне.")
def laba2_2_result():
    number = functions.input_checker("Введіть число: ", float)
    sum = 0
    kol = 0
    while number != 0:
        sum += number
        kol += 1
        number = functions.input_checker("Введіть число: ", float)
    average = sum / kol
    print("Сума: ", sum, "Кількість: ", kol, "Середнє арифметичне: ", average)
laba2_2_result()