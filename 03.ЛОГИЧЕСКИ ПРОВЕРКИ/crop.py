#     • 1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000];
#     • 2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00];
#     • 3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600];
#     • 4ти ред: брой работници – цяло число в интервала [1 … 20];


x = int(input("enter sk m vineyard between 10 nad 5000: "))
y = float(input("enter grapes per sq m between 0.00 and 10.00: "))
z = int(input("enter liters of wine needed for sale between 10 and 600: "))
n = int(input("enter number of workers between 1 and 20: "))

# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
# От 1 кв.м лозе се изкарват Y килограма грозде.
# За 1 литър вино са нужни 2,5 кг. грозде.
# Желаното количество вино за продан е Z литра.

crop = x * y
wine_crop = 0.4 * crop
wine_liter = wine_crop / 2.5

if wine_liter < z:
    dfc = z - wine_liter
    print("It will be a tough winter! More " + str("%.0f" % dfc) + " liters wine needed.")

elif wine_liter > z:
    print("Good harvest this year! Total wine: " + str("%.0f" % wine_liter) + " liters.")
    extra = wine_liter - z
    per_prsn = extra / n
    print(str("%.0f" % extra) + " liters left -> " + str("%.0f" % per_prsn) + " liters per person.")




