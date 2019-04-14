# въвежда час и минути от 24-часово денонощие и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат hh:mm.
# Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула когато е необходимо.

# enter h >> 0 <= h <= 23
# enter min >> 1 <= min <= 59


h = int(input())
min = int(input())
minadd15 = min + 15

if 0 <= min < 45 and 0 <= h < 23:
    print(str(h) + ":" + str(minadd15))


elif 45 <= min <= 54 and 0 <= h < 23:
    h += 1
    min -= 60
    print(str(h) + ":" + "0" + str((minadd15 - 60)))


elif 55 <= min <= 60 and 0 <= h < 23:
    h += 1
    min -= 60
    print(str(h) + ":" + str((minadd15 - 60)))


elif 0 <= min < 45 and h == 23:
    print(str(h) + ":" + str(minadd15))

elif 45 <= min <= 54 and h == 23:

    min -= 60
    print("0:") + "0" + str((minadd15 - 60))


elif 55 <= min <= 60 and h == 23:

    min -= 60
    print("0:" + str((minadd15 - 60)))










