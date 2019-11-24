
# 1 meter (m) >> 1000 millimeters (mm)
# 1 meter (m) >> 100 centimeters (cm)
# 1 meter (m) >> 0.000621371192 miles (mi)
# 1 meter (m) >> 39.3700787 inches (in)
# 1 meter (m) >> 0.001 kilometers (km)
# 1 meter (m) >> 3.2808399 feet (ft)
# 1 meter (m) >> 1.0936133 yards (yd)

# line 1 >> entry amount
# line 2 >>entry unit
# line3 >> exit amount and unit

nmbr = float(input())
from_metric = input()
to_metric = input()
to_m = 0
from_m = 0

# to convert from end metric unit to meter:
if from_metric == "m":
    to_m = nmbr / 1
elif from_metric == "mm":
    to_m = nmbr/1000
elif from_metric == "cm":
    to_m = nmbr/100
elif from_metric == "mi":
    to_m = nmbr/ 0.000621371192
elif from_metric == "in":
    to_m = nmbr/39.3700787
elif from_metric == "km":
    to_m = nmbr/0.001
elif from_metric == "ft":
    to_m = nmbr/3.2808399
elif from_metric == "yd":
    to_m = nmbr/1.0936133

# to convert from meter to end metric unit
if to_metric == "m":
    from_m = to_m * 1
elif to_metric == "mm":
    from_m = to_m * 1000
elif to_metric == "cm":
    from_m = to_m * 100
elif to_metric == "mi":
    from_m = to_m * 0.000621371192
elif to_metric == "in":
    from_m = to_m * 39.3700787
elif to_metric == "km":
    from_m = to_m * 0.001
elif to_metric == "ft":
    from_m = to_m * 3.2808399
elif to_metric == "yd":
    from_m = to_m * 1.0936133

print(from_m, to_metric)

