#send quirey to arduino over xbee modules to receive temperature and humidity
#without repeater
import serial
import time
import sys
ser=serial.Serial('/dev/ttyUSB0',9600)
ser.close()
ser.open()
time.sleep(1)
#ser.read()
sys.stdout.flush()
ser.flushInput()
ser.flushOutput()
def send_data():
    global c
    c=raw_input("enter A for tmperature of house1 and B for humidity, enter C for temperature of house2 and D for humidity:")
    ser.write((c))
    print c

def receive_data():
    while True:
        time.sleep(.5)
        a=ser.inWaiting()
        
        b=ser.read(a)
        time.sleep(1)
        print 'receiving data is from:',c
        print 'receiving data is:',b
send_data()
time.sleep(1)
sys.stdout.flush()
ser.flushInput()
ser.flushOutput()
receive_data()
    
    
    
