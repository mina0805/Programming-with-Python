student_grades = {
    'bob': [2,2],
    'petar':[5,2,5],
    'maria':[1,6,5,6],
    'alex':[2,2],
}

# 1 sort by key
sort_by_key = sorted(student_grades.items(), key = lambda kvp: kvp[0])
print(sort_by_key)

# 2 sort by value
sort_by_value = sorted(student_grades.items(), key = lambda kvp: kvp[1])
print(sort_by_value)

# 3 sort by value and then by key
sort_by_value_and_key = sorted(student_grades.items(), key = lambda kvp: (kvp[1], kvp[0]))
print(sort_by_value_and_key)

# 4 sorted by the length of the values and then by key
sorted_by_length = sorted(student_grades.items(), key = lambda kvp: (len(kvp[1]), kvp[0]))
print(sorted_by_length)

# 5 sort both key and value by descending order o
sorted_by_desc_ordr = sorted(student_grades.items(), key = lambda kvp: (len(kvp[1]), kvp[0]), reverse = True)
print(sorted_by_desc_ordr)
