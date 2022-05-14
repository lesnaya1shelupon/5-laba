import math
x = list(input().split(" "))
y = 0
x1 = []
w = 0
r = []

for i in x:
    if float(i) < 0 or int(i) < 0:
        y += 1
print("Количество отрицательных элемнтов:", y)
for l in x:
    x1.append(abs(float(l)))
m = min(x1)
for q in x1:
    if float(m) < float(q):
        w += float(q)
print("Сумма модулей элементов списка, расположенных после минимального по модулю элемента:", w)
for e in x:
    if float(e) < 0:
        r.append(float(e) ** 2)
print("Замена всех отрицательных чисел их квадратом и сортировка:", sorted(r))
