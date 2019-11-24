num = int(input())


edinitsi = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

desetitsi = ["", "", "twenty", "thirty", "fourty", "fify", "sixty", "seventy", "eighty", "ninety", "one hundred"]

if 1 <= num <= 19:
    print(edinitsi[num])
elif 20 <= num <= 100:
    if num % 10 == 0:
        print(desetitsi[num//10])
    elif num % 10 != 0:
        print(desetitsi[num // 10], edinitsi[num % 10])
elif num <= 0:
    print('invalid number')
elif num > 100:
    print('invalid number')













