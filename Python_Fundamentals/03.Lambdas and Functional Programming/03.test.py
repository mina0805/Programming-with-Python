student_grades = {
    'bob': [2,2],
    'petar':[5,2,5],
    'maria':[6,6,5,6],
    'alex':[2,2],
}

# 1 sort by key
sort_by_key = sorted(student_grades.items(), key = lambda kvp: kvp[0])
print(sort_by_key)

# 2 sort by value of the length of the list
sort_by_value = sorted(student_grades.items(), key = lambda kvp: kvp[1])
print(sort_by_value)

# 3 sort by value and then by key
sort_by_value_and_key = sorted(student_grades.items(), key = lambda kvp: (kvp[1], kvp[0]))
print(sort_by_value_and_key)