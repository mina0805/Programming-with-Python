chr = int(input())
roses = int(input())
tulips = int(input())
season = input().lower()
holiday = input().lower()
total_p = 0

if season == "summer" or season == "spring":
    chr_p = 2
    roses_p = 4.1
    tulip_p = 2.5
    total_p = chr * chr_p + roses * roses_p + tulips * tulip_p
    if holiday == "y":
        total_p *=1.15
        if tulips >= 7 and season == "spring":
            total_p *= 0.95
        if roses + chr + tulips >=20:
            total_p *= 0.8

elif season == "winter" or season == "autumn":
    chr_p = 3.75
    roses_p = 4.5
    tulip_p = 4.15
    total_p = chr * chr_p + roses * roses_p + tulips * tulip_p
    if holiday == "y":
        total_p *= 1.15
        if roses >=10 and season == "winter":
            total_p = total_p * 0.9
        if roses + chr + tulips >=20:
            total_p *= 0.8

print(total_p+2)

