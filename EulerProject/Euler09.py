import time
time.perf_counter()
for a in range(150,500):
    for b in range(150,500):
        for c in range(300,600):
            if a+b+c == 1000 and (a ** 2) + (b ** 2) == (c ** 2):
                print(a, b, c)
                print(a*b*c)
                print('готово', time.perf_counter())
                break