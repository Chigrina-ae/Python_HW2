# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.

# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчёте на одного сотрудника.

# 7 (Дополнительно). Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

# 1
# a = 1
# b = 1.2
# c = 'three'
# d = int(input('enter integer d '))
# e = input('enter string e ')
# print('a = ' , a)
# print('b = ' , b)
# print('c = ' , c)
# print('d = ' , d , ' e = ' , e)

# 2
# all_time = int(input('enter time in seconds = '))
# hours = all_time // 3600
# minutes = (all_time - hours * 3600)//60
# seconds = all_time - hours * 3600 - minutes * 60
# print(hours , ' : ' , minutes , ' : ' , seconds)

# 3
# n = input('enter integer number n = ')
# nn = n * 2
# nnn = n * 3
# print(n , ' + ' , nn , ' + ' , nnn , ' = ' , int(n)+int(nn)+int(nnn))

# 4
# n = input('enter integer positive number n = ')
#  n = int(n)
# if n > 0:
# copy_n = n
# max = 0
# while copy_n != 0:
# if max < copy_n % 10:
# max = copy_n % 10
# copy_n = copy_n // 10
# print('max number from n = ' , max)

# else:
# print ('invalid number')


# 5
# revenue = int(input('enter revenue = '))
# costs = int(input('enter costs = '))
# if revenue == costs:
# print('company does not profit or loss generated')
# elif revenue < costs:
# print('company loss generated')
# else:
# print('company profit generated')
# margin = (revenue - costs)/revenue
# print ('company_s margin = ' , margin , ' $')
# personal = int(input('how many people do work in company?'))
# profit_per_personal = (revenue - costs) / personal
# print('company_s profit per person' , profit_per_personal, ' $')

# 6
a = int(input('result in the first day = '))
b = int(input('target result = '))
days = 1
target = a
while target < b:
    target = target + target * 0.1
    days = days + 1
print('you need ', days, ' days')
