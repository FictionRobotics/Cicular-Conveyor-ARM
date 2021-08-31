from gpiozero import Servo, Motor
from time import sleep
import serial


port = serial.Serial("/dev/rfcomm2", baudrate=9600)

x=0


motor1 = Motor(20,21,16)

motor2 = Motor(26,19,13)

servo1 = Servo(17)

servo2 = Servo(27)

def armaction():

    servo2.value = -0.7

    sleep(2)

    servo1.value = -0.8

    sleep(2)

    servo2.value = 0.7

    sleep(2)

    servo1.mid()

    sleep(2)

    motor1.forward(0.2)

    sleep(0.86)

    motor1.stop()

    sleep(2)

    servo1.value = -0.6

    sleep(2)

    servo2.mid()

    sleep(2)

    servo1.mid()

    sleep(2)

    motor1.backward(0.2)
    
    sleep(0.84)

    motor1.stop()
    
    sleep(3)

    arm=1


def conveyer():
    motor2.forward(0.5)

    sleep(14.8)

    motor2.stop()

def main():
    
    y=0
  
    print("DIGITAL LOGIC -- > SENDING...")
    x=str('i')
    port.write(bytes(x,'utf-8'))

    rec = port.readline()

    if (rec == bytes("start\n","utf-8")):
        
        
        

        while(y<3):
        
            
            conveyer()
    
            sleep(1)
    
            armaction()

            print("CARGO PLACED ON DELIVERY BOT...")
          
            y = y +1

            x=0
            

if __name__ == "__main__":
    main()
