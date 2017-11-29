
# displays the distance in decimetres on a 7-segment display
from gpiozero import LED
from gpiozero import DistanceSensor
import time

seg = [LED(27,active_high=False),LED(25,active_high=False),LED(24,active_high=False),
      LED(23,active_high=False),LED(22,active_high=False),LED(18,active_high=False),
      LED(17,active_high=False)]

segmentPattern = [[0,1,2,3,4,5],[1,2],[0,1,6,4,3],[0,1,2,3,6],[1,2,5,6],[0,2,3,5,6], #0 to 5
                 [0,2,3,4,5,6],[0,1,2],[0,1,2,3,4,5,6],[0,1,2,5,6],[0,1,2,4,5,6], #6 to A
                 [2,3,4,5,6],[0,3,4,5],[1,2,3,4,6],[0,3,4,5,6],[0,4,5,6] ] #B to F

sensor = DistanceSensor(15,4)

def main() :
   print("Display distance on a 7-seg display")

   while 1:
       distance = sensor.distance * 10 # distance in decimeters
       print("distance",distance)
       if distance >= 10.0:
          distance = 16.0
       display(int(distance))    
       time.sleep(0.8)
          
def display(number):
    for i in range(0,7):
       seg[i].off()
    if number < 16:   
       for i in range(0,len(segmentPattern[number])):
           seg[segmentPattern[number][i]].on()
   
# Main program logic:
if __name__ == '__main__':   
    main()   