# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input("Введите натуральное число: "))
nums = []
a = 2
while a * a <= n:
        if n % a == 0:
            nums.append(a)
            n=n//a
        else:
            a += 1
nums.append(n)
print(nums)