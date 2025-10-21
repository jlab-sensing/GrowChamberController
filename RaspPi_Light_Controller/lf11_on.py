
import RPi.GPIO as GPIO
import serial
EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.HIGH)

t = serial.Serial("/dev/ttyS0",9600, timeout=5)

def send_signal(input:str):
        GPIO.output(EN_485,GPIO.HIGH)
        print (t.portstr)
        strInput = input + '\r\n'
        n = t.write(strInput.encode())
        print (n)
        GPIO.output(EN_485,GPIO.LOW)
        str = t.readline()
        print (str)
        return str



while (1):
        command = input('command:')
        send_signal(command)
