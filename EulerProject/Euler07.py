import time
a = [2]
a += [x for x in range(3,120000,2)]
time.perf_counter()
for x in a:
    for k in a:
        if k % x == 0 and k // x != 1:
            a.remove(k)

print(a[10000])
print('готово', time.perf_counter())
