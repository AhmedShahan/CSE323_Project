# Process BT AT TQ
TQ=2
a=[('p1',3,2),('p2',5,0),('p3',3,3),('p4',6,1)]
# Answer: p2 p4 p1 p3 p2 p4 p1 p3
# 0 2 4 6 8 10 12 13 14 15
OBT=[]
OLST=[]

# Collect all the Burst Time
for i in a:
    OBT.append(i[1])
    OLST.append(i[0])

# Sort using Arrival Time
a.sort(key = lambda x : x[2])
list1=[]
list2=[]
list3=[]
list4=[]
sortedOBT=[]
for i in a:
    sortedOBT.append(i[1])

# print(OBT)
# print(sortedOBT)
# print(a)
templist=[]
cycle=[]
for i in a:
    # print(i[1])
    value=i[1]
    process=i[0]
    t=value//TQ #2
    r=value%TQ  #1
    cycle.append(t+1)
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

# for i in Output:
#     print(i)

# print("Temp List:",templist)
# print("Output",Output)
# # print("Length ",len(templist))
FinalFinal=[]
for values in Output.values():
    print(values[2])
    # FinalFinal.append(values[1])
    # FinalFinal.append(values[1])
    # FinalFinal.append(values[2])
    # for i in values:
    #     print(i)

# print(values)
# print(FinalFinal)
# for i in templist:

# for i in templist:

#     if i[0]=="p1":
#         list1.append(i)
#     elif i[0]=="p2":
#         list2.append(i)
#     elif i[0]=="p3":
#         list3.append(i)
#     elif i[0]=="p4":
#         list4.append(i)
# print("list 1",list1)
# print("list 2",list2)
# print("list 3",list3)
# print("list 4",list4)
# firstList=[]
# count=0
# firstList.append(templist[0])
# for i in range(1,len(templist)):
#     if firstList.count(templist[i])>0:
#         count+=1
#         continue
#     else:
#         firstList.append(templist[i])
#         count+=1
# print(firstList)



# print(list1)
# print(list2)
# print(list3)
# print(list4)


    # for j in a:
    #     print(j[1])
    # while i[2]!=0:
    #     i[2]=i[2]-2
    #     if i<=0:
    #         print(0)
    #         break
    #     else:
    #         print(i)
# print(OBT)
# while all(item == 0 for item in a):
#     print(a)
#     a[1]=a[1]-1
# for i in OBT:
#     while True:
#         i=i-2
#         listi.append(a[])
#         if i<=0:
#             print(0)
#             break
#         else:








