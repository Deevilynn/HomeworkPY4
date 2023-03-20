# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# n = int(input('Enter quantity of elements in first set: '))
# n_set = set(input('Enter elements of first set. Split them with whitespace: ').split())
# if n != len(n_set):
#     print('Try again. Quantity of elements in first set doesn''t equel number of entered elements.')
# else:
#     m = int(input('Enter quantity of elements in second set: '))
#     m_set = set(input('Enter elements of second set. Split them with whitespace: ').split())
# if m != len(m_set):
#     print('Try again. Quantity of elements in second set doesn''t equel number of entered elements.')
# else:
#     print(sorted(n_set.union(m_set)))
   
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод

a = int(input())
a_list = list()
for i in range(a):
    b = int(input())
    a_list.append(b)

list_count = list()
for i in range(len(a_list)- 1):
    list_count.append(a_list[i - 1] + a_list[i] + a_list[i + 1])
list_count.append(a_list[-2] + a_list[-1] + a_list[0])
print(max(list_count))

