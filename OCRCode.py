import pytesseract
import time
from PIL import Image
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time

camera =PiCamera()
camera.rotation = 180

camera.start_preview()
sleep(10)
camera.capture('/home/pi/Makethon/capture.jpg')
camera.stop_preview()
img =Image.open ("WEZK8.png")
text = pytesseract.image_to_string(img, config="")
#text = "BIRAL CHAL JAA "
print(text)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


s11 = GPIO.PWM(11, 50)
s12 = GPIO.PWM(12, 50)

s21 = GPIO.PWM(15, 50)
s22 = GPIO.PWM(16, 50)

s11.start(2.5)
s12.start(2.5)
s21.start(2.5)
s22.start(2.5)

def setServoAngle(servo , angle):
    if(servo==1):
#         if(angle==0):
#             s11.ChangeDutyCycle(0)
#             s12.ChangeDutyCycle(0)
        if(angle<180):
            pwm = angle/18 + 2.5
            s11.ChangeDutyCycle(pwm)
        else:
            angle = angle - 180
            pwm = angle/18 +2.5
            s11.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            s12.ChangeDutyCycle(pwm)
    if(servo==2):
#         if(angle==0):
#             s11.ChangeDutyCycle(2.5)
#             s12.ChangeDutyCycle(2.5)
        if(angle<180):
            pwm = angle/18 + 2.5
            s21.ChangeDutyCycle(pwm)
        else:
            angle = angle - 180
            pwm = angle/18 +2.5
            s21.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            s22.ChangeDutyCycle(pwm)
    time.sleep(2)
    
def reset():
    setServoAngle(1,0)
    setServoAngle(2,0)
    
def pos_to_angle(pos):
    switcher = {
        0: 0.00,
        1: 22.5, 
        2: 67.5, 
        3: 112.5,
        4: 157.5,
        5: 202.5,
        6: 247.5,
        7: 292.5,
        8: 337.5,
        
    }
    
    return switcher.get(pos)
def Biral(i):
    s11.start(2.5)
    s12.start(2.5)
    s21.start(2.5)
    s22.start(2.5)


    ch=i

    if(ch=='A' or ch=='a'):
        setServoAngle(1,pos_to_angle(0))
        setServoAngle(2,pos_to_angle(3))
        time.sleep(2)
        reset()
    
 
    if(ch=='B' or ch=='b'):
        setServoAngle(1,pos_to_angle(7))
        setServoAngle(2,pos_to_angle(3))
        time.sleep(2)
        reset()
    
    if(ch=='C' or ch=='c'):
        setServoAngle(1,pos_to_angle(0))
        setServoAngle(2,pos_to_angle(6))
        time.sleep(2)
        reset()
    
    if(ch=='D' or ch=='d'):
        setServoAngle(1,pos_to_angle(0))
        setServoAngle(2,pos_to_angle(5))
        time.sleep(2)
        reset()
    if(ch=='E' or ch=='e'):
        setServoAngle(1,pos_to_angle(0))
        setServoAngle(2,pos_to_angle(1))
        time.sleep(2)
        reset()
    if(ch=='F' or ch=='f'):
        setServoAngle(1,pos_to_angle(7))
        setServoAngle(2,pos_to_angle(6))
        time.sleep(2)
        reset()
    if(ch=='G' or ch=='g'):
        setServoAngle(1,pos_to_angle(7))
        setServoAngle(2,pos_to_angle(5))
        time.sleep(2)
        reset()
    if(ch=='H' or ch=='h'):
        setServoAngle(1,pos_to_angle(5))
        setServoAngle(2,pos_to_angle(1))
        time.sleep(2)
        reset()
    
    if(ch=='I' or ch=='i'):
        setServoAngle(1,pos_to_angle(5))
        setServoAngle(2,pos_to_angle(6))
        time.sleep(2)
        reset()
    if(ch=='J' or ch=='j'):
        setServoAngle(1,pos_to_angle(5))
        setServoAngle(2,pos_to_angle(5))
        time.sleep(2)
        reset()
    if(ch=='K' or ch=='k'):
        setServoAngle(1,pos_to_angle(2))
        setServoAngle(2,pos_to_angle(3))
        time.sleep(2)
        reset()
    
    if(ch=='L' or ch=='l'):
        setServoAngle(1,pos_to_angle(4))
        setServoAngle(2,pos_to_angle(3))
        time.sleep(2)
        reset()
    
    if(ch=='M' or ch=='m'):
        setServoAngle(1,pos_to_angle(2))
        setServoAngle(2,pos_to_angle(6))
        time.sleep(2)
        reset()
    
    if(ch=='N' or ch=='n'):
        setServoAngle(1,pos_to_angle(2))
        setServoAngle(2,pos_to_angle(5))
        time.sleep(2)
        reset()

    if(ch=='o' or ch=='O'):
        setServoAngle(1,pos_to_angle(2))
        setServoAngle(2,pos_to_angle(1))
        time.sleep(2)
        reset()
    
    if(ch=='P' or ch=='p'):
        setServoAngle(1,pos_to_angle(4))
        setServoAngle(2,pos_to_angle(6))
        time.sleep(2)
        reset()
    
    if(ch=='Q' or ch=='q'):
        setServoAngle(1,pos_to_angle(4))
        setServoAngle(2,pos_to_angle(5))
        time.sleep(2)
        reset()
    
    if(ch=='R' or ch=='r'):
        setServoAngle(1,pos_to_angle(4))
        setServoAngle(2,pos_to_angle(1))
        time.sleep(2)
        reset()
    
    if(ch=='S' or ch=='s'):
        setServoAngle(1,pos_to_angle(3))
        setServoAngle(2,pos_to_angle(6))
        time.sleep(2)
        reset()
    
    if(ch=='T' or ch=='t'):
        setServoAngle(1,pos_to_angle(3))
        setServoAngle(2,pos_to_angle(5))
        time.sleep(2)
        reset()
    if(ch=='U' or ch=='u'):
        setServoAngle(1,pos_to_angle(2))
        setServoAngle(2,pos_to_angle(2))
        time.sleep(2)
        reset()
    
    if(ch=='V' or ch=='v'):
        setServoAngle(1,pos_to_angle(4))
        setServoAngle(2,pos_to_angle(2))
        time.sleep(2)
        reset()
    
    if(ch=='W' or ch=='w'):
        setServoAngle(1,pos_to_angle(5))
        setServoAngle(2,pos_to_angle(8))
        time.sleep(2)
        reset()
    
    if(ch=='X' or ch=='x'):
        setServoAngle(1,pos_to_angle(2))
        setServoAngle(2,pos_to_angle(4))
        time.sleep(2)
        reset()
    
    if(ch=='Y' or ch=='y'):
        setServoAngle(1,pos_to_angle(2))
        setServoAngle(2,pos_to_angle(8))
        time.sleep(2)
        reset()
    
    if(ch=='z' or ch=='Z'):
        setServoAngle(1,pos_to_angle(2))
        setServoAngle(2,pos_to_angle(7))
        time.sleep(2)
        reset()
    
    if(ch==' '):
        setServoAngle(1,pos_to_angle(8))
        setServoAngle(2,pos_to_angle(3))
        time.sleep(2)
        reset()
for i in text:
    print(i)
    reset()
    Biral(i)
    reset()
    
    
    