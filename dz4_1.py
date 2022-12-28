# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
a = float(input('Введите число для округления : '))
pi=math.pi
count=(len(str(a).split('.')[1]))
h = 0
b = list()
for x in str(pi):
    h += 1
    b.append(x)
    if h == count+2:
        break
h = ''.join(b)
print(h)




