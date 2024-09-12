#Soal 1
a = [1,2,3]
b = [4,5,6]

hasil = a + b


print(hasil)

def jumlahkan(list):
  total = 0
  for x in list:
    total += x
  print(total)

jumlahkan(hasil)

print(sum(hasil))

#Soal 2
import numpy as np

nilai_siswa = np.array([85, 55, 40, 90])
print(nilai_siswa[3])

nama = input("Masukkan nama anda: ")
nim = input("Masukkan NIM anda: ") 

print("Hello, World!")
print(f"Nama saya {nama}")
print(f"NIM saya {nim}")

#Soal 3
if 5 > 2:
  print("five is greater than 2")

x = 5
y = "john"
print(x)
print(y)

x = 4
y = "sally"
print(x)


#Soal 4
a = [1,2,3,4,5,6,7,8,9]

def getFirst(list):
  print(list[0])

def getSecond(list):
  print(list[1])

def getLast(list):
  print(list[-1])

getFirst(a)
getSecond(a)
getLast(a)



 
