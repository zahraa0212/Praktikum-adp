n = int(input("masukkan nilai n : "))
if n < 4:
    print("masukkan nilai n minimal adalah 4")
else:
    total_boom = 0
    nilai_tengah = int((n-1) / 2)
    for i in range(n):
        for j in range(n):
            if n % 2 == 1 and i == nilai_tengah and j == nilai_tengah :
                print("HORE", end="   ")
            elif i == j :
                print("1", end="      ")
            elif  (i + j) == (n - 1) :
                print("2", end="      ")
            else:
                print("BOOM", end="   ")
                total_boom = total_boom + 1
        print(  ) 
    print(f"total BOOM yang muncul = {total_boom}")