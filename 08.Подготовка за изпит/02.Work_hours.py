hours_needed = int(input())
workers = int(input())
days = int(input())
penalties = (hours_needed - (workers*days*8))*days

# 1 worker works 8 hours a day

if hours_needed <= workers*days*8:
    print(str(workers*days*9 - hours_needed) + " hours left")
else:
    print(str(hours_needed - (workers*days*8)) + " overtime")
    print("Penalties: " + str(penalties))

