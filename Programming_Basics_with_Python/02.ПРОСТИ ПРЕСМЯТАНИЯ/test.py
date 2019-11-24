USD = 1.79549
EUR = 1.95583
GBP = 2.53405
BGN = 1

amount = float(input())
cur_from = input()
cur_to = input()
input_amount = amount
output_amount = 1

if cur_from == "USD":
    input_amount *= 1.79549
elif cur_from == "EUR":
    input_amount *= 1.95583
elif cur_from == "GBP":
    input_amount *=2.53405
elif cur_from == "BGN":
    input_amount *= 1
amount = output_amount

if cur_to == "USD":
    output_amount /= 1.79549
elif cur_to == "EUR":
    output_amount /= 1.95583
elif cur_to == "GBP":
    output_amount /=2.53405
elif cur_to == "BGN":
    output_amount /= 1
final_amount = (amount*input_amount)/output_amount
print(final_amount)



#1 bgn = 1/1.79549
#12.35 eur to gbp
#print("%.2f" % ((12.35*1.95583)/2.53405))






