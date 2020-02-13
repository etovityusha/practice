a, b, c, sum = 1, 0, 0, 0
while c < 4000000:
    print(c, end=' ')
    c = a + b
    if c % 2 == 0:
        sum += c
    b = a
    a = c
print()
print(sum)