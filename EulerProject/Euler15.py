import time
n = int(input('Введите размер сетки: '))

A = []
for i in range(n+1):
    A.append([0 for x in range(n+1)])
for x in range(n+1):
    A[x][0] = 1
    A[0][x] = 1

i, j = 1,1
while i < n+1:
    while j < n+1:
        A[i][j] = A[i-1][j] + A[i][j-1]
        j += 1
    i += 1
    j = 1


print(A[n][n])