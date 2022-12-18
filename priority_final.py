def priority(maina) :
    #maina=[("p1",2,5,1),("p2",10,5,2),("p3",1,7,1),("p4",2,2,3),("p5",8,8,4)]

    copya=maina.copy()

    copya.sort(key = lambda x : x[0])
    copya.sort(key = lambda x : x[2])

    mainlist=[]
    ganNum=[]

    temp=copya[0]
    # print('Copy a',copya)
    mainlist.append(temp)

    copya.remove(copya[0])
    maina.remove(temp)
    # print(maina)

    templist=[]
    bt=mainlist[0][1]+mainlist[0][2]

    while (len(maina)!=0):
        for i in copya:
            if i[2]<=bt:
                templist.append(i)
                templist.sort(key = lambda x : x[2])
        if len(templist)==0:
            bt=bt+1
        else:
            # print(templist)
            temp=templist[0]
            mainlist.append(temp)
            templist=[]
            copya.remove(temp)
            maina.remove(temp)
            bt=bt+temp[1]
            # print(maina)
            # print(mainlist)
            templist=[]

    #print('-----------',mainlist)
    return(mainlist)