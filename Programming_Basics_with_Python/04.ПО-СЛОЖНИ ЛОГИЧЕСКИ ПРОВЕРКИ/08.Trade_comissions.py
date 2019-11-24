# 08. Commission
town = input().lower()
sales = float(input())
c = ""

if town == 'sofia':
    if 0<= sales <= 500:
        c = 0.05 * sales
    elif 500 < sales <= 1000:
        c = 0.07 * sales
    elif 1000 < sales <= 10000:
        c = 0.08 * sales
    elif sales > 10000:
        c = 0.12 * sales
    else:
        c = "error"

elif town == 'varna':
    if 0<= sales <= 500:
        c = 0.045 * sales
    elif 500 < sales <= 1000:
        c = 0.075 * sales
    elif 1000 < sales <= 10000:
        c = 0.1 * sales
    elif sales > 10000:
        c = 0.13 * sales
    else:
        c = "error"

elif town == 'plovdiv':
    if 0<= sales <= 500:
        c = 0.055 * sales
    elif 500 < sales <= 1000:
        c = 0.08 * sales
    elif 1000 < sales <= 10000:
        c = 0.12 * sales
    elif sales > 10000:
        c = 0.145 * sales
    else:
        c = "error"

else:
    c = 'error'
if c == 'error':
    print(c)
else:
    print("%.2f" % c)

