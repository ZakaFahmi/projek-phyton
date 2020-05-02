def bubbleSort(listData):
    print('Data yang akan diurutkan: ', listData)
    a=1
    for x in range(len(listData)-1,0,-1):
        print("iterasi ke-",a,"jumlah iterasi-",x)
        b=1
        for i in range(x):
            if listData[i]>listData[i+1]:
                listData[i],listData[i+1]=listData[i+1],listData[i]
                print("no=", b, listData)
            elif listData[i]<listData[i+1]:
                print("no=",b,listData)
            b+=1
        a+=1
        urut=int(1)
        for z in range(len(listData)-1):
            if listData[z] <= listData[z + 1]:
                urut=urut and 1
            else:
                urut = urut and 0
        if urut == 1:
            print("Data terurut =", listData)
            return

x = [100,34,1,7,2,4,6,77,4,54]
bubbleSort(x)

