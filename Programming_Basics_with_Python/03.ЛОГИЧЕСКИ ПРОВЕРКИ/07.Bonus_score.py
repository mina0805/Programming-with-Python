# base_points = int
# if base_points <= 100 >> + 5 points
# if 100 < Base_points <= 1000 >> + 20%
# if base_points > 1000 >> + 10%
# if base points are even >> + 1 point
# if base points end in 5 >> + 2 points

#base_points = 0
bonus_points = 0


base_points = int(input())

if base_points <= 100:
    bonus_points += 5
elif 100 < base_points <= 1000:
    bonus_points = 0.2 * base_points
elif base_points > 1000:
    bonus_points = 0.1 * base_points

if base_points % 2 == 0:
    bonus_points += 1
if base_points % 10 == 5:
    bonus_points += 2

total_points = base_points + bonus_points


print(bonus_points)
print(total_points)


