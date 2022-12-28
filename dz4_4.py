# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint
k = int(input('Введите натуральную степень k:'))
f=[randint(0,100) for i in range(k)]+[randint(1,100)]
poly=' + '.join([f'{(j,"")[j==0]}*x^{i}' for i, j in enumerate(f) if j][::-1])
poly = poly.replace('*x^0', '' );poly = poly.replace('^1', '' )  
print(f'{poly} = 0')   
with open('file.txt', 'w') as data:
    data.write(f'{poly} = 0')
data.close()



