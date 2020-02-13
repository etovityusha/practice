# https://pythonworld.ru/osnovy/tasks.html
#1
def arifmetic(a,b,operator):
    """
    Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть
    произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое
    на второе). В остальных случаях вернуть строку "Неизвестная операция".
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return  a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    return 'Неизвестная операция'

#2
def is_year_leap(year):
    """
    Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
    если год високосный, и False иначе.
    """
    if year // 4 and not year % 100 == 0 or year % 400 == 0:
        return True
    return False

#3
def square(a):
    """
    Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
    периметр квадрата, площадь квадрата и диагональ квадрата.
    """
    P = a * 4
    S = a * a
    c = ((a ** 2) + (a ** 2)) ** 0.5
    trpl = (P, S, c)
    return trpl

#4
def season(mounth):
    """
    Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому
    этот месяц принадлежит (зима, весна, лето или осень).
    """
    if 0 < mounth <= 2 or mounth == 12:
        return 'Зима'
    elif 3 <= mounth <= 5:
        return 'Весна'
    elif 6 <= mounth <= 8:
        return 'Лето'
    elif 9 <= mounth <= 1:
        return 'Осень'

#5
def bank(money, years):
    """
    Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада
    увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
    Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму,
    которая будет на счету пользователя.
    """
    for i in range(years):
        money = money * 1.1
    return int(money)

#6
def is_prime(number):
    """
    Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое,
    и False - иначе.
    """
    a = [2]
    a += [x for x in range(3, 1001, 2)]
    print(a)

    for i in a:
        for j in a:
            if j % i == 0 and j // i != 1:
                a.remove(j)
    if number in a:
        return True
    else:
        return False

#7
def date(day, mounth, year):
    """
    Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем
    календаре, и False иначе.
    """
    if mounth == 1 or  mounth == 3 or  mounth == 5 or  mounth == 7 or  mounth == 8 or  mounth == 10 or  mounth == 12  and 1 <= day <= 31:
        return True
    elif mounth == 2:
        if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
            if 1 <= day <= 29:
                return True
        if year % 4 != 0:
            if 1 <= day <= 28:
                return True
    elif mounth == 4 or mounth == 6 or mounth == 9 or mounth == 11  and 1 < day <= 30:
        return True
    return False

#8
def XOR_cipher(strng,key):
    """
    Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая
    возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом. Написать также
    функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
    """

