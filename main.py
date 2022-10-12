import math
from math import factorial
password = input('Подтвердите, что вы не робот, введите "@":')
if password != '@':
    print('Вы не прошли проверку, вы робот, тогда зачем вам калькулятор? :/')
else:
    print('Вы успешно прошли проверку!')
    print('Привет! Добро пожаловать в калькулятор.')
    retry = 1
    while retry == 1:
        print('Выберите действие, которое хотите совершить: \n'
              '+ : сложение;\n'
              '- : вычитание;\n'
              '/ : деление;\n'
              '* : умножение;\n'
              '** : возведение в степень;\n'
              'x : квадратное уравнение;\n'
              '< : минимальное число из 3-х;\n'
              'k : кол-во цифр в числе;\n'
              'n : сумма всех чисел от 1 до n; \n'
              'f : факториал.')
        operator = input()
        if operator == '+':
            number_1 = float(input('Введите первую переменную:'))
            number_2 = float(input('Введите вторую переменную:'))
            res = number_1 + number_2
            print('ответ = ', res)
        elif operator == '-':
            number_1 = float(input('Введите первую переменную:'))
            number_2 = float(input('Введите вторую переменную:'))
            res = number_1 - number_2
            print('ответ = ', res)

        elif operator == '*':
            number_1 = float(input('Введите первую переменную:'))
            number_2 = float(input('Введите вторую переменную:'))
            res = number_1 * number_2
            print('ответ = ', res)

        elif operator == '/':
            number_1 = float(input('Введите первую переменную:'))
            number_2 = float(input('Введите вторую переменную:'))
            res = number_1 / number_2
            print('ответ = ', res)

        elif operator == '**':
            number_1 = float(input('Введите первую переменную:'))
            number_2 = float(input('Введите вторую переменную:'))
            res = number_1 ** number_2
            print('ответ = ', res)

        elif operator == '<':
            def minimum(a=float(input("1-е число: ")), b=float(input("2-е число: ")), c=float(input("3-е число: "))):
                return min([a, b, c])
            print("минимальное число = ", minimum())

        elif operator == 'k':
            def kol(x=int(input("число: "))):
                return len(str(x))
            print("Кол-во = ", kol())

        elif operator == 'n':
            def summer(n=int(input("N = "))):
                return sum(range(1, n + 1))
            print("сумма всех чисел = ", summer())

        elif operator == 'f':
            def factor(f=int(input('число: '))):
                if f == 0:
                    return 1
                return factor(f - 1) * f
            print('факториал = ', factor())

        elif operator == 'x':
            a = float(input('Введите a:'))
            b = float(input('Введите b:'))
            c = float(input('Введите c:'))
            dt = b ** 2 - 4 * a * c
            if dt == 0:
                x1 = -b / (2 * a)
                print('x = ', x1)
            elif dt > 0:
                x1 = (-b + math.sqrt(dt)) / (2 * a)
                x2 = (-b - math.sqrt(dt)) / (2 * a)
                print('x1= ', x1, '\nx2= ', x2)
            else:
                print('Корней нет')

        else:
            print('неизвестная операция')
