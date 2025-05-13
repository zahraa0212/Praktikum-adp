nilai_x = [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
f_x = []
i = 0
while i < len(nilai_x):
    x = nilai_x[i]
    if x > 0:
        fx = x**3 - x
    elif x < 0:
        fx = 1 / (x**2)
    else:
        fx = 1
    f_x.append(fx)
    i = i + 1
print(f"| {"x":<5} | {"f(x)":<21} |")
i = 0
while i < len(nilai_x):
    print(f"| {nilai_x[i]:<5} | {f_x[i]:<21} |")
    i = i + 1