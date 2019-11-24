business_Days_month = int(input("Enter busines days per month: "))
daily_wage = float(input("Enter daily wage: "))
USD_to_BGN = float(input("Enter USD to BGN rate: "))

monthly_wage = business_Days_month * daily_wage
yearly_wage = (monthly_wage * 14 + monthly_wage/2)*0.75
yearly_wage_BGN_day = (yearly_wage * USD_to_BGN)/365
print("%.2f" % yearly_wage_BGN_day)

