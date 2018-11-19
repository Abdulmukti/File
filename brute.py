print("Brute Force")
l = [18, 15, 25, 16, 38,21]
print("before: ", l)
l.sort()
print("Brute : ", l)
print("min : ", l[0])
print("min : ", l[5])

print("Algoritma Greedy")
x = [18, 15, 25, 16, 38,21]
i=0
while i < len(x):
    j=0
    while j < i:
        if x[i] < x[j]:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
        j= j +1
    i= i +1
    print("langkah: ", x)
print('Greedy : ', x)
print('Max : ', x[0])
print('Max : ', x[5])

print("Devide and Conquer")
x = [18, 15, 25, 16, 38,21]
print(x)
i = len(x)
y = int(i/2)
a = x[:y]
b = x[y:]
kiri = print("kiri\t\t:",a)
print("kiri min\t:",a[0])
print("kiri maks\t:",a[2])
kanan = print("kanan\t\t:",b)
print("kanan min\t:",b[0])
print("kanan maks\t:",b[2])
