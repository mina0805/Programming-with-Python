raw_data = input().lower()
shells = {}
mylist = []

while raw_data != "aggregate":

    mylist = list(map(str.strip, raw_data.split(" ")))
    key = mylist[0]
    value = mylist[1]

# import list of year,value pairs

    for key,value in mylist:
        try:
            shells[key].append(value)
        except KeyError:
            shells[key] = [value]
    raw_data = input().lower()

for i in shells:
    print(i)



