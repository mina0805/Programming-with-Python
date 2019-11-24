n = int(input())

for num_1 in range(1,n+1):
    for num_2 in range(1,n+1):
        for num_3 in range(1,n+1):
            for num_4 in range(1,n+1):
                if n%num_1 == 0 and n%num_2 == 0 and n%num_3 == 0 and n % num_4 == 0:
                    print(str(num_1) +str(num_2) + str(num_3) + str(num_4), end=" ")
