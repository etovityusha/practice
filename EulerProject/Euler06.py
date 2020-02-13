n = int(input('Введите n:'))
sumkv = 0
kvsum = 0
for i in range (n+1):
    kvsum += i
kvsum **= 2
for i in range (n+1):
    sumkv += (i ** 2)
print ('Сумма квадратов = ', sumkv)
print ('Квадрат суммы = ', kvsum)
print ('Разница =', kvsum-sumkv)