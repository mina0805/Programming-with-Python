N1 = int(input())
N2 = int(input())
operator = input()

# +, -, * -> „{N1} {оператор} {N2} = {резултат} – {even/odd}“
# / -> „{N1} / {N2} = {резултат}“ ("%.2f" % result)
# % ->„{N1} % {N2} = {остатък}“
# N2 == 0 -> „Cannot divide {N1} by zero“

if operator == "+":
        if (N1 + N2) % 2 == 0:
            print(str(N1) + " + " + str(N2) + " = " + (str(N1 + N2)) + " - even")
        elif (N1 + N2) % 2 == 1:
            print(str(N1) + " + " + str(N2) + " = " + (str(N1 + N2)) + " - odd")

elif operator == "-":
        if (N1 - N2) % 2 == 0:
            print(str(N1) + " - " + str(N2) + " = " + (str(N1 - N2)) + " - even")
        elif (N1 - N2) % 2 == 1:
            print(str(N1) + " - " + str(N2) + " = " + (str(N1 - N2)) + " - odd")

elif operator == "*":
        if (N1 * N2) % 2 == 0:
            print(str(N1) + " * " + str(N2) + " = " + (str(N1 * N2)) + " - even")
        elif (N1 * N2) % 2 == 1:
            print(str(N1) + " * " + str(N2) + " = " + (str(N1 * N2)) + " - odd")

elif operator == "/":
    if N2 != 0:
        print(str(N1) + " / " + (str(N2)) + " = " + (str("%.2f" % (N1 / N2))))
    elif N2 == 0:
        print('Cannot divide ' + str(N1) + ' by zero')

elif operator == "%":
    print(str(N1) + " % " + (str(N2)) + " = " + (str(N1 % N2)))






