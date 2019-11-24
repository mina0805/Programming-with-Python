n = int(input())

f0 = 0
f1 = 1

for num in range(n):
    f1 = f0 + f1
    f0 = f1 - f0
    print(f1)
