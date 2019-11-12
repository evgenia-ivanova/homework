"""
Увести з клавіатури величини двох кутів трикутника (в градусах).
Визначити, чи існує такий трикутник, і якщо так, то чи буде він прямокутним.
"""
from Validators import functions

functions.inform(1, 2, "Визначити чи існує трикутник та чи є він прямокутним.")
def lab1_2_result():
    angle1 = functions.input_checker("Введіть величину кута 1: ", float, lambda angle1: angle1 > 0)
    angle2 = functions.input_checker("Введіть величину кута 2: ", float, lambda angle2: angle2 > 0)
    if (angle1 + angle2) == 90 or angle1 == 90 or angle2 == 90:
        print("Трикутник існує і є прямокутним")
    elif (angle1 + angle2) >= 180 or (angle1 + angle2) <= 0:
        print("Трикутник не існує")
    else:
        print("Трикутник існує, але не є прямокутним")
functions.start_program(lab1_2_result)
