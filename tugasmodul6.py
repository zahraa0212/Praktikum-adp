x = [0, 0, 0]
y = [0, 0, 0]
print("masukkan titik pertama")
x[0] = float(input("masukkan nilai x1 : "))
y[0] = float(input("masukkan nilai y1 : "))
print("masukkan titik kedua")
x[1] = float(input("masukkan nilai x2 : "))
y[1] = float(input("masukkan nilai y2 : "))
print("masukkan titik ketiga")
x[2] = float(input("masukkan nilai x3 : "))
y[2] = float(input("masukkan nilai y3 : "))
titik1 = (x[0] - x[1])**2 + (y[0] - y[1])**2
titik2 = (x[1] - x[2])**2 + (y[1] - y[2])**2
titik3 = (x[2] - x[0])**2 + (y[2] - y[0])**2
if titik1 == titik2 or titik1 == titik3 or titik2 == titik1 :
    print("ketiga titik tersebut sama kaki")
else :
    print("ketiga titik tersebut tidak sama kaki")