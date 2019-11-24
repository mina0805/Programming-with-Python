n = int(input("Enter business days per month: "))
m = float(input("Enter money earned per day: "))
rate = float(input("Enter BGN/USD exchange tate: "))

monthly_wage = n*m
bonus = n*m*2.5
gross_anual_income = monthly_wage*14.5
net_anual_income = 0.75 * gross_anual_income
avg_daily_wage = net_anual_income/365
avg_daily_wage_bgn = avg_daily_wage*rate
print('%.2f' % avg_daily_wage_bgn)
