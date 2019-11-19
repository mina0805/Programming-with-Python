n = int(input())
top_student = 0
between_4_and_499 = 0
between_3_and_399 = 0
fail = 0
average = 0
for i in range(1, n+1):
    grade = float(input())
#    Ред 1 - "Top students: {процент студенти с успех 5.00 или повече}%"
#   Ред 2 - "Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
#    Ред 3 - "Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
#    Ред 4 - "Fail: {по-малко от 3.00}%"
#    Ред 5 - "Average: {среден успех}"

    if 0<= grade <= 2.99:
        fail += 1
    elif 3.00 <= grade <= 3.99:
        between_3_and_399 += 1
    elif 4.00 <= grade <= 4.99:
        between_4_and_499 += 1
    elif 5.00 <= grade <= 6.00:
        top_student += 1
    average = grade/n
#print(fail)
#print(between_3_and_399)
#print(between_4_and_499)
#print(top_student)

print(("Top students: " + (str('{0:.2%}'.format(top_student/n)))))
print(("Between 4.00 and 4.99: " + (str('{0:.2%}'.format(between_4_and_499/n)))))
print(("Between 3.00 and 3.99: " + (str('{0:.2%}'.format(between_3_and_399/n)))))
print(("Fail: " + (str('{0:.2%}'.format(fail/n)))))
print(average)


