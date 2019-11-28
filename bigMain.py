#IF GIVING ERROR, THEN RUN AGAIN UNTIL NO ERROR (MAX 2 MORE TIMES)

from adafruit_rplidar import RPLidar
import time
import math

#Definitions

#Example of Processing Scan Data
def process_data(scan_data):
    
    for x in range(0,len(scan_data)):
        #print(str(x)+': '+str(scan_data[x]))
        pass

#Now the Code

#Don't Change This
port_name = '/dev/ttyUSB0'

#Basic Initialization
sumlist = [] #Data Array
sumnum = 0
a=0.0
b=0.0
c=0.0

#Class Call Speedups
sa = sumlist.append
tt = time.time
mf = math.floor

#RPLidar Hardware Initialization
lidar = RPLidar(None, port_name)
lis = lidar.iter_scans

#DANGER!!!
#lidar.set_pwm(1023)

#Initalising Size
scan_data = [0]*400

#Getting Scan Data Loop
try:
    for scan in lis(): #Wait for Rotation to Complete
        a=tt() #Start Time
        
        #Offloading Scan Data
        for (_, angle, distance) in scan: #Offloading Scan Data
            scan_data[min([399, mf(angle)])] = distance
            
        #Now Call the Useful Data Processing
        process_data(scan_data)
        
        #Adding Statistical Timing Analysis
        b=tt()
        c=b-a
        sa(c)
        sumnum+=1
        print(c)

eoxcept KeyboardInterrupt: #CTRL-C Handler
    print('Stopping!')
    print('Avg: ')
    print(sum(sumlist)/sumnum)
    print('Max: ')
    print(max(sumlist))
    print('Min: ')
    print(min(sumlist))
    
#MANDATORY!!!
lidar.stop()
lidar.set_pwm(0)
lidar.disconnect()
