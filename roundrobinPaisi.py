
global chart
Chart=[]
class Process:
    def __init__(self,pid,AT,BT):
        self.pid=pid
        self.arrival=AT
        self.burst=BT

def shiftCL(alist):
    temp= alist[0]
    for i in range(len(alist)-1):
        alist[i]=alist[i+1]
    alist[len(alist)-1]=temp
    return alist

def RR(tq,plist,n):
    queue=[]
    time=0
    ap=0
    rp=0
    done=0
    q=tq
    start=0
    while(done<n):

        for i in range(ap,n):
            if time>=plist[i].arrival:
                queue.append(plist[i])
                ap+=1
                rp+=1
        if rp<1:
            Chart.append(0)
            time+=1
            continue
        if start:
            queue=shiftCL(queue)

        if queue[0].burst>0:
            if queue[0].burst>q:
                for g in range (time,time+q):
                    Chart.append(queue[0].pid)
                time+=q 
                queue[0].burst -=q 
            else:
                for g in range(time, time+queue[0].burst):
                    Chart.append(queue[0].pid)
                time+=queue[0].burst
                queue[0].burst=0
                done+=1
                rp-=1
            start=1


plist=[]
plist.append(Process(1,0,5))
plist.append(Process(2,1,3))
plist.append(Process(3,3,6))
plist.append(Process(4,4,1))
plist.append(Process(5,6,4))

result= RR(3,plist,len(plist))
print(result) 