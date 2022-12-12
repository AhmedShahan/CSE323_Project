# import fcfs as fcfs

# print("1. FCFS\n")
# print("2. SJF\n")
# print("3. Priority\n")
# print("4. RR\n")
# algorithm=input("Enter Algorithm")
# algorithm=int(algorithm)

# if algorithm==1 or 2:
#     print("Enter Process Details")
#     mainList=[]
#     for i in range(0,5):
#         processId=input("Enter Process Id: ")
#         bt=input("Enter BT: ")
#         bt=int(bt)
#         at=input("Enter AT: ")
#         at=int(at)
#         mainList.append((processId,bt,at))

# elif algorithm==3:
#     print("Enter Process Details")
#     mainList=[]
#     for i in range(0,5):
#         processId=input("Enter Process Id: ")
#         bt=input("Enter BT: ")
#         bt=int(bt)
#         at=input("Enter AT: ")
#         at=int(at)
#         priority=input("Enter AT: ")
#         mainList.append((processId,bt,at,priority))

# if algorithm==1:
#     result=fcfs.algorithm(mainList)

# elif algorithm==2:
#     result=fcfs.algorithm(mainList)
# print(result)
