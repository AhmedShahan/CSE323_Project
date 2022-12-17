import tm1637
from machine import Pin
from utime import sleep
import math
def statusvalue1(bt):
    BT=bt
    val=math.ceil(((100/BT)*BT))
    for i in range(BT,val+1):
        tm = tm1637.TM1637(clk=Pin(0), dio=Pin(1))
        tm.number(i)
        sleep(0.1)

def statusvalue2(bt):
    BT=bt
    val=math.ceil(((100/BT)*BT))
    for i in range(BT,val+1):
        tm = tm1637.TM1637(clk=Pin(3), dio=Pin())
        tm.number(i)
        sleep(0.1)

def statusvalue3(bt):
    BT=bt
    val=math.ceil(((100/BT)*BT))
    for i in range(BT,val+1):
        tm = tm1637.TM1637(clk=Pin(3), dio=Pin(2))
        tm.number(i)

        
def statusvalue4(bt):
    BT=bt
    val=math.ceil(((100/BT)*BT))
    for i in range(BT,val+1):
        tm = tm1637.TM1637(clk=Pin(3), dio=Pin(2))
        tm.number(i)

def statusvalue5(bt):
    BT=bt
    val=math.ceil(((100/BT)*BT))
    for i in range(BT,val+1):
        tm = tm1637.TM1637(clk=Pin(3), dio=Pin(2))
        tm.number(i)


result= [('p2', 10, 7),('p1', 7, 5)]
for i in result:
    if i[0]=='p1':
        statusvalue1(i[1])
    if i[0]=='p2':
        statusvalue2(i[1])
    else:
        break