'''
Напишите программу, которая найдёт произведение
пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

size = int(input('Задайте размер списка:' + " "*2))
test_list = []

for i in range(size):
    print(f'Введите {i + 1} элемент:\t', end="")
    item = int(input())
    test_list.append(item)

result = 0
result_list = []
for i in range(size):
    if i <= len(test_list) - 1:
        result = test_list[i] * test_list[len(test_list) - 1]
        result_list.append(result)
        test_list.pop()
print(result_list)
