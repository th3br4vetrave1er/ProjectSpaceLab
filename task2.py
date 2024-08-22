# 🟡 Задача 2 - Растения против Зомби

# Создайте функцию, которая будет принимать в себя два массива несортированных чисел 
# (первый - защищающийся массив растений, второй - атакующий массив зомби) и вернёт boolean значение 
# в зависимости от того победили ли защитники.

# ➡️ Условия:

# Каждый элемент массива атакует элемент другого массива с тем же индексом массива. Выживший - это число с наибольшим значением.
# Если значение одинаковое, они оба погибают.
# Если одно из значений отсутствует (различная длина массивов), солдат с непустым значением выживает.
# Чтобы выжить, обороняющаяся сторона должна иметь больше выживших, чем атакующая сторона.
#  В случае, если с обеих сторон одинаковое количество выживших, побеждает команда с наибольшей начальной силой атаки. 
#  Если общая сила атаки обеих сторон одинакова, верните True.
# Начальная сила атаки представляет собой сумму всех значений в каждом массиве.

