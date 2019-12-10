str_input = input()
Dict = dict((x.strip(), y.strip()) for x, y in (element.split('=') for element in str_input.split(', ')))

print(Dict)
