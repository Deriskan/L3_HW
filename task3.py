# Задание 3

# 1. Напишите счетчик с помощью конструкции while, который выводит числа от 0 до 10.

print('--- 1 ---')

i = 0
while 0 <= i <= 10:
    print(i)
    i += 1

# 2. Напишите счетчик с помощью конструкции while, который выводит числа от 20 до 1.

print('--- 2 ---')

i = 20
while 1 <= i <= 20:
    print(i, end=' ')
    i -= 1

# 3. Напишите цикл while, в котором вы, если число чётное, каждую итерацию уменьшаете его в 2 раза. Т.е. вы делите
# целое чётное число на 2 пока от него не останется нечётный остаток. Посчитайте сколько раз вы делили нацело на 2.

print('\n--- 3 ---')

while True:
    try:
        n = int(input('Enter Integer:\n'))
        break
    except ValueError:
        print('It\'s NOT an Integer!')

c = 0  # Счетчик для выполненных операций деления.

while n % 2 == 0:
    n /= 2  # Операция над числом.
    c += 1  # Увеличение счетчика на 1.

print('Division by 2, counter: ', c)