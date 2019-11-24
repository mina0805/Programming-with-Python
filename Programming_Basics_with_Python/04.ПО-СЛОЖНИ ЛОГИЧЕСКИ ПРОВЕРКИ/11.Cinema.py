show = input().lower()
raw = int(input())
col = int(input())
total = 0

if show == "Premiere":
    total = raw * col * 12.00
elif show == "Normal":
    total = raw * col * 7.50
else:
    total = raw * col * 5.00

print((str("{:.2f}".format(total))) + " leva")

