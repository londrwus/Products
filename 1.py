with open('vacancy_new.csv', encoding='utf-8-sig') as file: # открыть CSV файл
    col_names = file.readline()
    rows = file.readlines()  # считывать разделы

rows = [s.split(';') for s in rows]
rows = [[a, b, c, d, e] for a, b, c, d, e in rows] # Все 5 разделов берем в массив двумерный
print(rows)
total = [] # будем брать туда значения из категории закусок
sum_val = 0 # итоговая сумма total
for i in range(len(rows)):
    if rows[i][0] == 'Закуски': # если из категории закуски, то будем считать total
        total.append(float(rows[i][3]) * float(rows[i][4]))

for j in range(len(total)):
    sum_val += total[j]

print(sum_val) # 87795.0 ответ