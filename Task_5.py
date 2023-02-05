'''
Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''
k = int(input('Введите количество элементов:' + " "*3))

nega_fibo_list = []
a, b = 1, 1
for i in range(k):
    nega_fibo_list.append(a)
    a, b = b, a + b
a, b = 0, 1
for i in range (k + 1):
    nega_fibo_list.insert(0, a)
    a, b = b, a - b

print(nega_fibo_list)