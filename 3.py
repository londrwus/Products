with open('products.csv', encoding='utf-8-sig') as file: # открыть CSV файл
    col_names = file.readline()
    rows = file.readlines()  # считывать разделы

rows = [s.split(';') for s in rows]
rows = [[a, b, c, d, e] for a, b, c, d, e in rows] # Все 5 разделов берем в массив двумерный
print(rows)
total = []
count = 0
category = ''
product = ''
unit = 0
for i in range(len(rows)):
    if rows[0][4] > sum_val:
        count = rows[0][3]
        category = rows[0][0]
        product = rows[0][1]

for j in range(len(total)):
    sum_val += total[j]

print("В категории ", category, " товар: ", product, " был куплен раз", count)