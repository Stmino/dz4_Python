# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import re
import itertools
with open('pol1.txt', 'r') as data:
        pol1 = data.read()
data.close()
with open('pol2.txt', 'r') as data:
        pol2 = data.read()
data.close()
pol11 = pol1.replace('= 0', '')
pol11 = re.sub("[*|^| ]", " ", pol11).split('+')
pol11 = [char.split(' ') for char in pol11]
pol11 = [[x for x in list if x] for list in pol11]
for i in pol11:
        if i[0] == 'x':i.insert(0, 1)
        if i[-1] == 'x':i.append(1)
        if len(i) == 1:i.append(0)
pol11 = [tuple(int(x) for x in j if x != 'x') for j in pol11]
print(pol1)
pol12 = pol2.replace('= 0', '')
pol12 = re.sub("[*|^| ]", " ", pol12).split('+')
pol12 = [char.split(' ') for char in pol12]
pol12 = [[x for x in list if x] for list in pol12]
for i in pol12:
        if i[0] == 'x':i.insert(0, 1)  
        if i[-1] == 'x':i.append(1)
        if len(i) == 1:i.append(0)
pol12 = [tuple(int(x) for x in j if x != 'x') for j in pol12]
print(pol2)
x = [0] * (max(pol12[0][1], pol11[0][1] + 1))
for i in pol11+pol12:        
        x[i[1]] += i[0]
sum_pol1 = [(x[i], i) for i in range(len(x)) if x[i] != 0]
sum_pol1.sort(key = lambda r: r[1], reverse = True)
x1 = ['*x^'] * len(sum_pol1);x2 = [x[0] for x in sum_pol1];x3 = [x[1] for x in sum_pol1]
sum_pol2= [[str(a), str(b), str(c)] for a, b, c in (zip(x2, x1, x3))]
for x in sum_pol2:
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
sum_pol2= list(itertools.chain(*sum_pol2))
sum_pol2[-1] = ' = 0'
final="".join(map(str, sum_pol2))
print(final)
with open('sum_pol.txt', 'w') as data:
        data.write(final)
data.close()  

