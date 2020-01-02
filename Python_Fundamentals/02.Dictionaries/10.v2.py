raw_data = input()
shells = {}


while raw_data != "Aggregate":
    region, size = raw_data.split()
    if region not in shells:
        shells[region] = []
    if int(size) not in shells[region]:
        shells[region].append(int(size))

    raw_data = input()
for key in shells:
    giant_shell = (sum(shells[key]) - int((sum(shells[key])//len(shells[key]))))

    print(f'{key} -> ', end='')
    print(f'{str(shells[key])}', end='')
    print(f' ({giant_shell})')

