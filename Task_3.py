'''
Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу
между максимальным и минимальным значением дробной части
элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
# test_list = [1.1, 1.2, 3.1, 5, 10.01]
# test_list = [2.2, 2.4, 1.01, 3.2, 7, 20.02, 4]
test_list = [2, 0.1, 2.04, 1.3, 10.61, 0.5, 4, 3.1]

# Решение №1
fraction_mini = test_list[1] - int(test_list[1])
fraction_maxi = 0

for i in test_list:
    if fraction_mini > i - int(i) and (i - int(i)) > 0:
        fraction_mini = i - int(i)

for i in test_list:
    if fraction_maxi < i - int(i):
        fraction_maxi = i - int(i)

dif = fraction_maxi - fraction_mini
print(f"{test_list} => {round(dif, 2)}\n")

# Решение №2
fraction = []
for i in test_list:
    a = i - int(i)
    if a > 0:
        fraction.append(round(a, 2))

mini = min(fraction)
maxi = max(fraction)
result = maxi - mini

print(f"{test_list} => {round(result, 2)}")
