
# p4
# p1
# p3

# Process Birstime Allocation
def algorithm(a):
    # a=[("4",10,2),("3",3,5),("1",7,2),("2",9,0),("5",12,6)]
    # print("Process|\tAllocation Time|Burst Time")

    # for i in range(0, len(a)):
    #     for j in range(0,3):
    #         print(a[i][j],end="\t")
    #     print('\n')

    a.sort(key = lambda x : x[0])

    a.sort(key = lambda x : x[2])
    print(a)


    allocation=[]

    #first allocation time in gang chart
    first=a[0][2]
    print(first)
    allocation.append(first)

    second=a[0][2] + a[0][1]
    print(second)
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