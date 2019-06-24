n = int(input())
l = int(input())
first_letter = 97
last_letter = 97+l

for num_1 in range(1,n):
    for num_2 in range(1,n):
        for num_3 in range(97,last_letter):
            for num_4 in range(97, last_letter):
                for num_5 in range(1, n+1):
                    if num_5 > num_1 and num_5 > num_2:
                        print(str(num_1) + str(num_2) + chr(num3) + chr(num_4) + str(num_5), "", end="")
