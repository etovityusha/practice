import time
a = True
n = 20
start_time = time.perf_counter()
while a == True:
    if n % 19 == 0:
        if n % 18 == 0:
            if n % 17 == 0:
                if n % 16 == 0:
                    if n % 15 == 0:
                        if n % 14 == 0:
                            if n % 13 == 0:
                                if n % 12 == 0:
                                    if n % 11 == 0:
                                        break
    n += 20
print(n)
print("{:g} s".format(time.perf_counter() - start_time))
