n = int(input())
odd_sum = 0
even_sum = 0
odd_max = -9999999999999999
even_max = -1000000000000
odd_min = 9999999999
even_min = 1000000000

if n == 0:
    odd_max = "No"
    even_max = "No"
    odd_min = "No"
    even_min = "No"

elif n == 1:
    num1 = float(input())
    odd_sum = num1
    odd_max = num1
    odd_min = num1
    even_max = "No"
    even_min = "No"
    even_sum = "No"
else:
    for i in range(1, n+1):
        num = float(input())

        if i % 2 == 1 and n != 1:
            odd_sum += num
            if num > odd_max:
                odd_max = num
            if num < odd_min:
                odd_min = num

        elif i % 2 == 0:
            even_sum += num
            if num > even_max:
                even_max = num
            if num < even_min:
                even_min = num

if type(odd_min) != str:
    odd_min = format(float(odd_min), 'g')
if type(odd_max) != str:
    odd_max = format(float(odd_max), 'g')
if type(even_min) != str:
    even_min = format(float(even_min), 'g')
if type(even_max) != str:
    even_max = format(float(even_max), 'g')

# removes floating zeros
# ako e 5.000 I ima {:g} ste go napravi 5, ako nyama {:g} ste e 5.0

print("OddSum = {:g}".format(odd_sum))
print("OddMin =", odd_min)
print("OddMax =", odd_max)
print("EvenSum = {:g}".format(even_sum))
print("EvenMin =", even_min)
print("EvenMax =", even_max)







