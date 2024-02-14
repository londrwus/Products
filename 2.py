with open('products.csv', encoding='utf-8-sig') as file: # открыть CSV файл
    col_names = file.readline()
    rows = file.readlines()  # считывать разделы

rows = [s.split(';') for s in rows]
rows = [[a, b, c, d, e] for a, b, c, d, e in rows] # Все 5 разделов берем в массив двумерный
print(rows)
total = []
sum_val = 0
category = ''
unit = 0
for i in range(len(rows)):
    if rows[0][4] > sum_val:
        sum_val = rows[0][3]
        category = rows[0][0]
        unit = rows[0][4]

for j in range(len(total)):
    sum_val += total[j]

print("В категории ", category, " самый дорогой товар: ", sum_val, " его цена за единицу товара составляет", unit)