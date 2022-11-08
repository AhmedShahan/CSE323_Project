
# p4
# p1
# p3

# Process Birstime Allocation
a=[("p4",10,2),("p3",3,5),("p1",7,2),("p2",9,0),("p5",12,6)]
# print("Process|\tAllocation Time|Burst Time")

# for i in range(0, len(a)):
#     for j in range(0,3):
#         print(a[i][j],end="\t")
#     print('\n')

a.sort(key = lambda x : x[0])

a.sort(key = lambda x : x[2])

print(a)


allocation=[]

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