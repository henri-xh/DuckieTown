import RPI.GPIO as G
from time import sleep

G.setwarnings(False)
G.cleanup()
G.setmode(G.BCM)



#1st set
G.setup(22, G.OUT) #No.15
G.setup(23, G.OUT) #No.16
G.setup(27, G.OUT) #No.13
#GND No.14


#2nd set
G.setup(10, G.OUT) #No.19
G.setup(9, G.OUT) #No.21
G.setup(25, G.OUT) #No.22
#GND No.20


#3rd set
G.setup(26, G.OUT) #No.37
G.setup(20, G.OUT) #No.38
G.setup(21, G.OUT) #No.40
#GND No.39


#4th set
G.setup(0, G.OUT) #No.27
G.setup(5, G.OUT) #No.29
G.setup(1, G.OUT) #No.28
#GND No.30


running = True
count = 0

while running:
    
    
    #1st set
    G.output(22, G.HIGH)
    sleep(10)
    G.output(22, G.LOW)
    print ('Red_1 done.')
    
    G.output(23, G.HIGH)
    sleep(10)
    G.output(23, G.LOW)
    print ('Green_1 done.')

    G.output(27, G.HIGH)
    sleep(1.5)
    G.output(27, G.LOW)
    print ('Yellow_1 done.')
    
    
    #3rd set
    G.output(26, G.HIGH)
    sleep(10)
    G.output(26, G.LOW)
    print ('Red_3 done.')
    
    G.output(20, G.HIGH)
    sleep(10)
    G.output(20, G.LOW)
    print ('Green_3 done.')

    G.output(21, G.HIGH)
    sleep(1.5)
    G.output(21, G.LOW)
    print ('Yellow_3 done.')
    
    
    
    
    #2nd set
    G.output(9, G.HIGH)
    sleep(10)
    G.output(9, G.LOW)
    print ('Green_2 done.')

    G.output(25, G.HIGH)
    sleep(1.5)
    G.output(25, G.LOW)
    print ('Yellow_2 done.')
    
    G.output(10, G.HIGH)
    sleep(10)
    G.output(10, G.LOW)
    print ('Red_2 done.')
    
    
    #4th set
    G.output(5, G.HIGH)
    sleep(10)
    G.output(5, G.LOW)
    print ('Green_4 done.')
    
    G.output(1, G.HIGH)
    sleep(1.5)
    G.output(1, G.LOW)
    print ('Yellow_4 done.')
    
    G.output(0, G.HIGH)
    sleep(10)
    G.output(0, G.LOW)
    print ('Red_4 done.')