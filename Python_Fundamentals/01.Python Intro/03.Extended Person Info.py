name = input()
age = int(input())
town = input()
salary = float(input())
age_range = 0.00
salary_range = 0.00

if age < 18:
    age_range = "teen"
elif 18 == age < 70:
    age_range = 'adult'
else:
    age_range = 'elder'

if salary < 500:
    salary_range = 'low'
elif 500 == salary <= 2000:
    salary_range = 'medium'
else:
    salary_range = 'high'
print('Name:',name)
print(f'Age:',age)
print(f'Town:',town)
print(f'Salary: ${salary:.2f}')
print(f'Age range:',age_range)
print(f'Salary range:',salary_range)

