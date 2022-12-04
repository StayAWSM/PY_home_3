import random as r

# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# # стоящих на нечётной позиции.
# # Пример:
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
# lst = [r.randint(1, 10) for i in range(1, r.randint(5, 8))]
# # Заполняем список случайной длины случайными значениями
# print(lst)
# print(f'Сумма элементов на нечетных позициях (индексах) равна {sum(lst[1::2])}')


# # Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# # минимальным значением дробной части элементов.
# # Пример:
# # - [1.1, 1.2, 3.1, 10.01] => 0.19
#
# float_list = [round(_ - int(_), 2) for _ in [1.1, 1.2, 3.1, 10.01]]
# print(float_list)
# print(round(max(float_list) - min(float_list), 3))


# # Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# # Пример:
# # - 45 -> 101101
# # - 3 -> 11
# # - 2 -> 10
#
# number = int(input())
# result = ''
# while number > 0:
#     result += str(number % 2)
#     number //= 2
#
# print(result[::-1])  # или print(bin(number)[2:])


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def reversed_fibonacci(n):
    if n in (1, 2):
        return 1
    return reversed_fibonacci(n + 2) - reversed_fibonacci(n + 1)

def negafibonacci() -> list:
    a = []
    b = []
    try:
        n = int(input("Введите число для последовательности Фибоначчи:"))
        if type(n) in [int]:
            for i in range(-n, n + 1):
                if i > 0:
                    a.append((fibonacci(i)))
                else:
                    b.append(reversed_fibonacci(i))
            return f'- для k={n} список будет выглядеть так: {b + a}'
    except ValueError as e:
        print(e)
        return negafibonacci()

print(negafibonacci())
