def bubbleSort(urut,mulai,listData):
    print('Data yang akan diurutkan: ', listData)
    if (urut=="asc" and mulai=="1") or (urut=="decs" and mulai=="2"):
        a=1
        for x in range(len(listData)-1,0,-1):
            print("iterasi ke-",a,"jumlah iterasi-",x)
            b=1
            for i in range(x):
                if listData[i]>listData[i-1]:
                    listData[i],listData[i+1]=listData[i+1],listData[i]
                    print("no=", b, listData)
                elif listData[i]<listData[i+1]:
                    print("no=",b,listData)
                b+=1
            a+=1
    else:
        a=1
        for x in range(len(listData)-1,0,-1):
            print("iterasi ke-",a,"jumlah iterasi-",x)
            b=1
            for i in range(x):
                if listData[i]<listData[i+1]:
                    listData[i],listData[i-1]=listData[i-1],listData[i]
                    print("no=", b, listData)
                elif listData[i]>listData[i+1]:
                    print("no=",b,listData)
                b+=1
            a+=1
    print("data terurut=",listData)
    
x = [10,2,1,13,15,22,11,45]
data1=input("silahkan pilih asc/decs=")
data2=input("masukkan angka 1/2=")
bubbleSort(data1,data2,x)
