'''
Напишите программу, которая будет преобразовывать
 десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

number_in = int(input('Введите десятичное число:' + " "*2))
out_bin = ''
binary_list = []

while number_in > 0:
    out_bin = str(number_in % 2) + out_bin
    number_in = number_in // 2
binary_list.append(out_bin)

print(f"[{''.join(binary_list)}]")