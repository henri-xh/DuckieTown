import RPI.GPIO as G
from time import sleep

G.setwarnings(False)
G.cleanup()
G.setmode(G.BCM)



#1st set
G.setup(27, G.OUT) #r1
G.setup(22, G.OUT) #y1
G.setup(23, G.OUT) #g1


#2nd set
G.setup(4, G.OUT) #r2
G.setup(14, G.OUT) #y2
G.setup(15, G.OUT) #g2


#3rd set
G.setup(26, G.OUT) #r3
G.setup(20, G.OUT) #y3
G.setup(21, G.OUT) #g3


#4th set
G.setup(5, G.OUT) #r4
G.setup(6, G.OUT) #y4
G.setup(12, G.OUT) #g4


running = True
count = 0

while running:
    
    
    G.output(27, G.HIGH) #r1
    G.output(26, G.HIGH) #r3
    G.output(15, G.HIGH) #g2
    G.output(12, G.HIGH) #g4
    sleep(10)
    G.output(27, G.LOW) #r1
    G.output(26, G.LOW) #r3
    G.output(15, G.LOW) #g2
    G.output(12, G.LOW) #g4
   
    
    G.output(22, G.HIGH) #y1
    G.output(20, G.HIGH) #y3
    G.output(14, G.HIGH) #y2
    G.output(6, G.HIGH) #y4
    sleep(1.5)
    G.output(22, G.LOW) #y1
    G.output(20, G.LOW) #y3
    G.output(14, G.LOW) #y2
    G.output(6, G.LOW) #y4


    G.output(23, G.HIGH) #g1
    G.output(21, G.HIGH) #g3
    G.output(4, G.HIGH) #r2
    G.output(5, G.HIGH) #r4
    sleep(10)
    G.output(23, G.LOW) #g1
    G.output(21, G.LOW) #g3
    G.output(4, G.LOW) #r2
    G.output(5, G.LOW) #r4
   
