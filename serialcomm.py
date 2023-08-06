import serial.tools.list_ports
import numpy as np
from matplotlib import pyplot as plt
from drone import *
import time

def serialcom():
    ports=serial.tools.list_ports.comports()
    serialInst=serial.Serial()
    distance=np.zeros(360)
    ang=np.zeros(360)
    caught = 1
    prev_distance = np.zeros(360)  # array to store previous distance values
    for i in range(360):
        ang[i]=i
    portList=[]
    #print(ang)
    for oneport in ports:
        portList.append(str(oneport))
        print(str(oneport))

    serialInst.baudrate=115200
    serialInst.port="COM5"
    serialInst.open()

    while (caught!= 0):
        try:
            packet=serialInst.readline()
            val=str(packet.decode('UTF-8','ignore'))
            indexa=val.find("A")
            indexb=val.find("B")
            indexc=val.find("C")
            indexd=val.find("D")
            dist=float(val[0:indexa])
            angle=round(float(val[indexa+1:indexb]))-360
            start=int(val[indexb+1:indexc])
            quality=int(val[indexc+1:indexd])
            caught = 0
        except:
            caught=1

    # print distance

    #print(distance)
    distance[angle]=dist 
    # shift the current distance array to the previous distance array
    prev_distance = np.copy(distance)

    while True:
        start_time = time.time() # record start time
        while (time.time() - start_time) < 1000: # execute for 2 seconds
            if serialInst.in_waiting:
                packet=serialInst.readline()
                val=str(packet.decode('UTF-8','ignore'))
                indexa=val.find("A")
                indexb=val.find("B")
                indexc=val.find("C")
                indexd=val.find("D")
                dist=float(val[0:indexa])
                angle=round(float(val[indexa+1:indexb]))-360
                start=int(val[indexb+1:indexc])
                quality=int(val[indexc+1:indexd])
                # print distance
                distance[angle]=dist 
                #print(distance)
            else:
                continue
            # motion detection

        
            diff_distance = np.abs(distance - prev_distance)
            # consider only those angles that are present in both the current and previous arrays
            valid_angles = np.intersect1d(np.where(distance > 0), np.where(prev_distance > 0))
            # find the angle with the maximum distance change
            max_change_angle = valid_angles[np.argmax(diff_distance[valid_angles])]
            max_change_value = diff_distance[max_change_angle]
            print("Max change angle:", max_change_angle)
            print("Max change value:", max_change_value)
            print("Quality:", quality)
            prev_distance = np.copy(distance)
            if(max_change_value>100)&(max_change_value<5000)&(distance[max_change_angle]<5000)&(max_change_angle>10):
                detector(distance[max_change_angle],max_change_angle)

            # shift the current distance array to the previous distance array
            
                
            plt.axes(projection = 'polar')
            plt.polar(ang,distance)
            #plt.show()
            #plt.savefig("mygraph.png")
