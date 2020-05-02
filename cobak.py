def bubbleSort(listData):
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
x = [10,2,1,13,15,22,11,45]
bubbleSort(x)
