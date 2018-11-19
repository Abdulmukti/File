koin=[5,4,3,1]
hasil=[]
jumlah = 0

for i in range(len(koin)):
    #i=0
    if hasil != 0 and (i < len(koin)):
        i+=1
        #print("koin \t", koin[i])
    else:
        hasil = hasil - koin[i]
        jumlah = jumlah + 1
        print(koin[i])
    #print (i)
