OBT=[]
def RRalgorithm(a,tq):
    # Process BT AT TQ
    TQ=tq
    # a=[('p1',3,2),('p2',5,0),('p3',3,3),('p4',6,1),('p5',6,1)]
    OLST=[]

    # Collect all the Burst Time
    for i in a:
        OBT.append(i[1])
        OLST.append(i[0])

    # Sort using Arrival Time
    a.sort(key = lambda x : x[2])
    list1=[]
    sortedOBT=[]
    sortedP=[]
    for i in a:
        sortedOBT.append(i[1])
        sortedP.append(i[0])

    # print(OBT)
    # print(sortedOBT)
    # print(a)
    templist=[]
    maxCycle=[]
    for i in a:
        # print(i[1])
        value=i[1]
        process=i[0]
        t=value//TQ #2
        maxCycle.append(t)
        r=value%TQ  #1
        for i in range(0,t):
            templist.append((process,TQ))
        if r!=0:
            templist.append((process,r))
        
    Output = {}
    for x, y in templist:
        if x in Output:
            Output[x].append((x, y))
        else:
            Output[x] = [(x, y)]
    # print(Output)
    mainList=[]
    maxTuple=max(maxCycle)
    list1.append(Output.get(sortedP[0]))
    list1.append(Output.get(sortedP[1]))
    list1.append(Output.get(sortedP[2]))
    list1.append(Output.get(sortedP[3]))
    list1.append(Output.get(sortedP[4]))
    # print("After Append",list1)
    ultapalta=("0",0)
    for i in list1:
        if len(i)<maxTuple:
            for j in range(0,maxTuple-len(i)):
                i.append(ultapalta)
    # print("Append Ultapalta",list1)
    for i in range(0,maxTuple):
        for j in range(0,5):
            temp=list1[j][i]
            if temp==("0",0):
                pass
            else:
                mainList.append(list1[j][i])
    # print(mainList)
    return mainList
    
# def OriginalBT():
#     return OBT



