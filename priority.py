
# Process Birstime Allocation priority
a=[("p1",5,2,2),("p2",7,2,1),("p3",2,1,3),("p4",3,3,0)]

a.sort(key = lambda x : x[2])
gann=[]
gann.append(a[0])

a.remove(a[0])
a.sort(key = lambda x : x[0])
a.sort(key = lambda x : x[3])

#print(a)
for i in range(0,len(a)):    
    gann.append(a[i])

print(gann)    
allocation=[]

#first allocation time in gang chart
first=gann[0][2]
allocation.append(first)

second=gann[0][2] + gann[0][1]
allocation.append(second)

for i in range(1,len(gann)):
    second=second+gann[i][1]
    allocation.append(second)

print(allocation)

sum=0
for i in range(0,len(gann)):
    sum=sum+(allocation[i]-gann[i][2])

awt=float(sum)/len(gann)

print(awt)