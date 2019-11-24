# p - praznitsi v koito NE sa sybota ili nedelya
# h - weekends k' si pytuva do rodniya grad
# играе волейбол само през уикендите и в празничните дни.
# Влади играе в София всяка събота, когато не е на работа и не си пътува до родния град,
# i 2/3 от празничните дни.
# Той пътува до родния си град h пъти в годинатаi igrae в неделя.
# Влади не е на работа 3/4 от уикендите, в които е в София.
# Отделно, през високосните години Влади играе с 15% повече волейбол от нормалното.
# Приемаме, че годината има точно 48 уикенда,­ подходящи за волейбол.
# kolko pyti v godina igrae?
year = input()
holidays = int(input())
homeweekends = int(input())

# igrae v sofia = ((48 - h) * 3/4) + h (2/3 * p)
# igrae v rodniya grad = h

import math
sf_wkds_pl = (48 - homeweekends) * 3.0/4
holidays_pl = holidays * 2.0/3
tot_dys_pl = sf_wkds_pl + holidays_pl + homeweekends

if year == 'leap':
    tot_dys_pl *= 1.15
print(math.floor(tot_dys_pl))
















