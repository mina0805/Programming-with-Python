n = int(input())

odd_sum = 0
even_sum = 0

for i in range(1, n+1):
    num = int(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

diff = abs(odd_sum - even_sum)

if odd_sum == even_sum:
    print("Yes")
    print('Sum = ' + str(odd_sum))
elif odd_sum != even_sum:
    print("No")
    print("Diff = " + str(diff))

