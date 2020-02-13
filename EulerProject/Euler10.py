import time
n = 2000000
lst = [2]
time.perf_counter()
for i in range(3, n + 1, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for j in lst:
        if j * j - 1 > i:
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
sum = 0
for i in lst:
    sum += i
print(sum)
print('готово', time.perf_counter())
