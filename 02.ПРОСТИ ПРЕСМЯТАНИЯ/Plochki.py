N = int(input("enter playground side: "))
W = float(input("enter plochka width: "))
L = float(input("enter ploachka length: "))
M = int(input("enter bench width: "))
O = int(input("enter bench length: "))
time_per_plochka = 0.2
area_to_cover = N * N - M * O
plochka_area = W * L
NumberPlochki = area_to_cover/plochka_area
print(str(NumberPlochki) + " blocks")
Time = NumberPlochki * 0.2
TimeInMin = ("%.2f" % Time)
print(str(TimeInMin) + " minutes")



