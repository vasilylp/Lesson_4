"""Задача 22:

Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
все те числа, которые встречаются в обоих наборах.Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств"""

# n, m = [int(z) for z in input("Введите размеры списков - две цифры через запятую : ").split(',')]
# print(n,m)
# n_list = list(int(num) for num in input(f"Введите {n} элементов 1 списка через пробел : ").strip().split())[:n]
# m_list = list(int(num) for num in input(f"Введите {m} элементов 2 списка через пробел : ").strip().split())[:m]
# print("n_list: ", n_list)
# print("m_list: ", m_list)
# set_1 = set(n_list)
# set_2 = set(m_list)
# list_1 = set_1
# list_2 = set_2
# list_3 = [n for n in list_1 if n in list_2]
# print(list_3)

# 2 solution Standart sample ___________________________________________________
mol = [int(x) for x in input("Введите число :").split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input("Введите число :").split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [int(x) for x in input("Введите число :").split()]
k = set(b)
for i in k:
    set_2.add(i)
lok =set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end = ' ')