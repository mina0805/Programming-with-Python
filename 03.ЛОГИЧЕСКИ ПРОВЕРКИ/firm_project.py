#     • На първия ред са необходимите часовете – цяло число в интервала [0 ... 200 000]
#     • На втория ред са дните, с които фирмата разполага – цяло число в интервала [0 ... 20 000]
#     • На третия ред е броят на служителите, работещи извънредно – цяло число в интервала [0 ... 200]

# През 10% от дните служителите са на обучение и не могат да работят по проекта.
# Един нормален работен ден във фирмата е 8 часа.
# Всеки служител може да работи по проекта в извънработно време по 2 часа на ден.

h = int(input("enter hours needed between 0 and 200,000: "))
d = int(input("enter days available between 0 and 20,000: "))
n = int(input("enter number of workers between 0 and 200: "))

h_worked = d * 0.9 * 8 + n * 2 * d
rem = h_worked - h

if h_worked >= h:
        print("Yes! " + str("%.0f" % rem) + " hours left.")

elif h_worked < h:
    nsf = rem * (-1)
    print("Not enough time! " + str("%.0f" % nsf) + " hours needed.")


