# Задача №1: Вычислить число c заданной точностью d. 

#from math import pi

#d =  int(input("Введите число для заданной точности числа Пи:\n"))
#print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# Задача №2: Задать натуральное число N. Написать программу, 
# которая составит список простых множителей числа N.


#num = int(input("Введите число: "))
#i = 2 # первое простое число
#lst = []
#old = num
#while i <= num:
    #if num % i == 0:
        #lst.append(i)
        #num //= i
        #i = 2
    #else:
        #i += 1
#print(f"Простые множители числа {old} приведены в списке: {lst}")

# Задача №3: Задать последовательность чисел. 
# Написать программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

#lst = list(map(int, input("Ввести числа через пробел:\n").split()))
#print(f"Исходный список: {lst}")
#new_lst = []
#[new_lst.append(i) for i in lst if i not in new_lst]
#print(f"Список из неповторяющихся элементов: {new_lst}")

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.    

#from random import randint
#max_val = 100
#k = int (input('Введите натуральную степень k:'))

#from random import randint
#import itertools

#k = randint(2, 7)

#def get_ratios(k):
    #ratios = [randint(0, 10) for i in range (k + 1)]
   # while ratios[0] == 0:
        #ratios[0] = randint(1, 10) 
    #return ratios

#def get_polynomial(k, ratios):
    #var = ['*x^']*(k-1) + ['*x']
    #polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    #for x in polynomial:
        #x.append(' + ')
    #polynomial = list(itertools.chain(*polynomial))
    #polynomial[-1] = ' = 0'
    #return "".join(map(str, polynomial)).replace(' 1*x',' x')


#ratios = get_ratios(k)
#polynom1 = get_polynomial(k, ratios)
#print(polynom1)

#with open('Polynomial.txt', 'w') as data:
   # data.write(polynom1)
#k = randint(2, 5)

#ratios = get_ratios(k) 
#polynom2 = get_polynomial(k, ratios)
#print(polynom2)

#with open('Polinomial2.txt', 'w') as data:
    #data.write(polynom2)

# Задача №5: Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random

def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)
def rnd():
    return random.randint(0,100)
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst 
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 
    ii = l-1 
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    



k1 = int(input("Ввести натуральную степень для первого файла k = "))
k2 = int(input("Ввести натуральную степень для второго файла k = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("file1.txt", create_str(koef1))
write_file("file2.txt", create_str(koef2))

# нахождение суммы многочлена

with open('file1.txt', 'r') as data:
    st1 = data.readlines()
with open('file2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_file("file3.txt", create_str(lst_new))
with open('file3.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")