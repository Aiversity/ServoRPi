import RPi.GPIO as GPIO
import time


devicelist = []
global i 
i = 0

def attach(name, pin, frequency):
    i =  i + 1
    print(i)
    devicelist.append(name)
    for x in range(len(devicelist)): 
        print(devicelist[x])
    
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, frequency)
#    exec(x, None)
    
    

def startposition(name2, pos):
    global servopos
    servopos = 1
    currentservo = eval(device[name])

#    angle = eval(angle)
    if pos != 1:
        servopos = 0.06 * pos
        servopos = servopos + 1
        servopos = round(servopos, 2)
        print(servopos)
        print('came')
     #   for x in devicelist:
      #      if x == name2:
  #              pwm.start(servopos)
       #         time.sleep(0.5)
#    else:
       # for x in devicelist:
        #    if x == name2:
 #               pwm.start(1)
         #       time.sleep(0.5)
    return servopos
   


def write(angle):
    servoangle = 1
#    angle = eval(angle)
    if angle != 1:
        servoangle = 0.06 * angle
        servoangle = servoangle + 1
        servoangle = round(servoangle, 2)
        print(servoangle)
        print('came')
    #    pwm.ChangeDutyCycle(servoangle)
   # else:
   #     pwm.ChangeDutyCycle(1)

    return servoangle

        


# while True:
#     if 0 < i < 14:
#         pwm.ChangeDutyCycle(i)
#         print(i , '=' , j)
#         time.sleep(0.5)
#         i = i + 0.07
#         i = round(i, 2)
#         j = j + i

