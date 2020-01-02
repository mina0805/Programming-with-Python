raw_data = input().lower()
shells = {}
size = []

while raw_data != "aggregate":
    key, value = raw_data.split()
    shells = raw_data[0]
    size = raw_data[1]
    raw_data = input()

    print(shells)
    print(size)





