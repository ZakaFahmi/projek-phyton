def bubbleSort(urut,mulai,listData):
    print("pakai=",urut,"No",mulai)
    print("data awal=",listData)
    if urut=="asc":
        if mulai=="1":
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
        else:
            a=1
            c=len(listData)-1
            for x in range(0,len(listData)-1):
                print("iterasi ke-",a,"jumlah iterasi-",c)
                b=1
                for i in range(len(listData)-1,x,-1):
                    if listData[i]<listData[i-1]:
                        listData[i],listData[i-1]=listData[i-1],listData[i]
                        print("no=", b, listData)
                    elif listData[i]>listData[i-1]:
                        print("no=",b,listData)
                    b+=1
                a+=1
                c-=1
    else:
        if mulai=="1":
            a=1
            c=len(listData)-1
            for x in range(0,len(listData)-1):
                print("iterasi ke-",a,"jumlah iterasi-",c)
                b=1
                for i in range(len(listData)-1,x,-1):
                    if listData[i]>listData[i-1]:
                        listData[i],listData[i-1]=listData[i-1],listData[i]
                        print("no=", b, listData)
                    elif listData[i]<listData[i-1]:
                        print("no=",b,listData)
                    b+=1
                a+=1
                c-=1
        else:
            a=1
            for x in range(len(listData)-1,0,-1):
                print("iterasi ke-",a,"jumlah iterasi-",x)
                b=1
                for i in range(x):
                    if listData[i]<listData[i+1]:
                        listData[i],listData[i+1]=listData[i+1],listData[i]
                        print("no=", b, listData)
                    elif listData[i]>listData[i+1]:
                        print("no=",b,listData)
                    b+=1
                a+=1
    print('Data hasil=: ', listData)
   
a = [10,2,1,13,15,22,11,45]
bubbleSort("asc","1",a)
print(" ")
b = [10,2,1,13,15,22,11,45]
bubbleSort("asc","2",b)
print(" ")
c = [10,2,1,13,15,22,11,45]
bubbleSort("decs","1",c)
print(" ")
d = [50,45,2,30,23,9] 
bubbleSort("decs","2",d)
