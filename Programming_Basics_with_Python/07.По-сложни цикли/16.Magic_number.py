n = int(input())

for num_1 in range(1,n+1):
    for num_2 in range(1,n+1):
        for num_3 in range(1,n+1):
            for num_4 in range(1,n+1):
                for num_5 in range(1,n+1):
                    for num_6 in range(1,n+1):
                        if num_1*num_2*num_3*num_4*num_5*num_6 == n:
                            print(str(num_1) +str(num_2) + str(num_3) + str(num_4) + str(num_5) + str(num_6), end=" ")
