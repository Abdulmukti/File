def binary(list,item):
    awal = 0
    akhir = len(list)-1
    temu = 0

    while awal <= akhir and not temu:
        tengah = (awal + akhir)//2
        if list[tengah] == item:
            temu = True
        else :
            if item < list[tengah]:
                last = tengah - 1
            else :
                awal = tengah + 1

    return temu

x = [0,1,2,8,13,17,19,32,42]
print(binary(x, 3))
print(binary(x,13))
