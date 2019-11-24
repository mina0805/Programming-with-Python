price_per_kg_Vegetable = float(input("enter price per kg vegetables: "))
price_per_kg_Fruit = float(input("enter price per kg fruit: "))
total_kg_Vegetables = int(input("enter total kg vegetables sold: "))
total_kg_Fruit = int(input("enter total fruit sold: "))
Total_income_in_Eur = int((price_per_kg_Vegetable * total_kg_Vegetables + price_per_kg_Fruit * total_kg_Fruit)/1.94)
TotalEUR =("%.2f" % Total_income_in_Eur)
str = str(TotalEUR) + " EUR"
print(str)









