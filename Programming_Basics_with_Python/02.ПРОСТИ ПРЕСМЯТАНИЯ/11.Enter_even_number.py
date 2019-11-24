n = float(input("Enter even number: "))
if n%2 == 0:
    print('Even number entered: ' + (str("%.0f" % n)))
elif n%2 != 0 and n%2 != 1:
    print('Invalid number!')
else:
    while n%2 ==1:
        print("The number is not even.")
        n = float(input("Enter even number: "))

    #print("Even number entered: " + format(n), 'g')
