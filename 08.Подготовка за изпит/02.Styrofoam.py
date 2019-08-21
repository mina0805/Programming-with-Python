budget = float(input())
house_area = float(input())
windows = int(input())
styrofoam_sq_m = float(input())
styrofoam_pcg_prc = float(input())

import math
# 1 window - 2.4 sq m
net_house_area = (house_area - windows*2.4)*1.2
styrofoam_nbr_pcg = math.ceil(net_house_area/styrofoam_sq_m)
total_price = styrofoam_pcg_prc*styrofoam_nbr_pcg
if total_price <= budget:
    print("Spent: " + str("%.2f"% total_price))
    print("Left: "+ (str("%.2f" %(budget-total_price))))
else:
    print("Need more: " + (str("%.2f" %(total_price - budget))))
