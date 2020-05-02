import random
import time
def urut(listData):
    print('Data yang akan diurutkan: ', listData)
    awal=time.time()
    for x in range(len(listData)-1,0,-1):
        for i in range(x):
            if listData[i]>listData[i+1]:
                listData[i],listData[i+1]=listData[i+1],listData[i]
            elif listData[i]<listData[i+1]:
                continue
            akhir=time.time()
    print(akhir-awal)
    return listData

data=[]
for i in range(1000):
    angka=random.randint(1,1000)
    data.append(angka)
print(data)
print(" ")
print(urut(data))
