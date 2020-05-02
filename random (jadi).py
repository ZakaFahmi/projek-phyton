import random
import time
def urut(listData):
    awal = time.time()
    print('Data yang akan diurutkan: ', listData)
    for x in range(len(listData)-1,0,-1):
        for i in range(x):
            if listData[i]>listData[i+1]:
                listData[i],listData[i+1]=listData[i+1],listData[i]
            elif listData[i]<listData[i+1]:
                continue
            akhir=time.time()
    print("waktu",akhir-awal,"detik")
    return listData

data=[]
loop=random.randint(1000,2000)
for i in range(loop):
    angka=random.randint(1,1000)
    data.append(angka)
print("hasilnya adalah",urut(data))
