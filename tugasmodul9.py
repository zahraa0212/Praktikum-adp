import time
import os
from termcolor import colored

teks = "   Happy Eid   "
lebar = 18
total_langkah = 20
delay = 1
teks_panjang = teks* 5 

i = 0
while i < total_langkah:
    os.system("cls")  
    potongan = teks_panjang[i:i+lebar]  
    print(colored(potongan, "cyan", "on_magenta"))  
    time.sleep(delay)
    i = i + 1