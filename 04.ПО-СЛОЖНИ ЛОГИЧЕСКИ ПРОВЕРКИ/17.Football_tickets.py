#     • VIP – 499.99 лева.
#     • Normal – 249.99 лева.
#1 до 4 – 75% от бюджета.
# • От 5 до 9 – 60% от бюджета.
  #  • От 10 до 24 – 50% от бюджета.
   # • От 25 до 49 – 40% от бюджета.
    #• 50 или повече – 25% от бюджета.
# “Yes! You have {N} leva left.
# Not enough money! You need {М} lev

budget = float(input())
category = input().lower()
people = int(input())
# budget_t = budget for tickets = budget from input - transport
budget_t = 0

if 1 <= people <= 4:
    budget_t = 0.25 * budget
elif 5 <= people <= 9:
    budget_t = 0.4 * budget
elif 10 <= people <= 24:
    budget_t = 0.5 * budget
elif 25 <= people <= 49:
    budget_t = 0.6 * budget
elif people > 50:
    budget_t = 0.75 * budget

if category == 'vip':
    if budget_t / 499.99 >= people:
        print('Yes! You have ' + (str("%.2f" % (budget_t - (499.99 * people)) + ' leva left.')))
    elif budget_t/499.99 < people:
        print('Not enough money! You need ' + (str("%.2f" % ((499.99 * people) - budget_t) + ' leva')))

elif category == 'normal':
    if budget_t / 249.99 >= people:
        print('Yes! You have ' + (str("%.2f" % (budget_t - (249.99 * people)) + ' leva left.')))
    elif budget_t/249.99 < people:
        print('Not enough money! You need ' + (str("%.2f" % ((249.99 * people) - budget_t) + ' leva')))




