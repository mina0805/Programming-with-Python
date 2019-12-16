guests_or_stop = input().lower()
action = False

size = length * width
while not action:
    if guests_or_stop != "stop":
        size = size - int(guests_or_stop)

        if size <= 0:
            print(f'No more cake left! You need {abs(size)} pieces more.')
            action = True
    else:
        print(f"{size} pieces are left.")
        break
    guests_or_stop = input().lower()
















