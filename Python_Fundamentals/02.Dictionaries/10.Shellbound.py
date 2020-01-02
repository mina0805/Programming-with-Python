raw_data = input().lower()
shells = {}


while raw_data != "aggregate":
    lst = list(map(str.strip, raw_data.split(" ")))
    dict_key = lst[0]
    dict_value = lst[1]
    if dict_key not in shells:
        shells[dict_key] = int(dict_value)
    else:
        if __name__ == '__main__':
            shells[dict_key] =
    raw_data = input().lower()

for item in shells:
    print(item)

print(shells)

#If I can rephrase your question,
# what you want is a dictionary with the years as keys
# and an array for each year containing a list of values associated with that year, right? Here's how I'd do it:

years_dict = dict()

for line in list:
    if line[0] in years_dict:
        # append the new number to the existing array at this slot
        years_dict[line[0]].append(line[1])
    else:
        # create a new array in this slot
        years_dict[line[0]] = [line[1]]



