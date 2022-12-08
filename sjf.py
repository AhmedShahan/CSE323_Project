


# Process Birstime Allocation

def sjf():
    a=[("p1",7,5),("p2",10,7),("p3",12,2),("p4",4,3),("p5",8,6)]
    a.sort(key = lambda x : x[0])
    a.sort(key = lambda x : x[1])
    a.sort(key = lambda x : x[2])

    print(a)


    allocation=[]

    #first allocation time in gang chart
    first=a[0][2]
    allocation.append(first)

    second=a[0][2] + a[0][1]
    allocation.append(second)

    for i in range(1,len(a)):
        second=second+a[i][1]
        allocation.append(second)

    print(allocation)

    sum=0
    for i in range(0,len(a)):
        sum=sum+(allocation[i]-a[i][2])

    awt=float(sum)/len(a)

    print(awt)
    return a