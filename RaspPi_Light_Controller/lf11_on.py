
import RPi.GPIO as GPIO
import serial
import argparse
from time import sleep


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


def on():
    send_signal("lo 2000")
    sleep(1)
    send_signal("ls all")

def off():
    send_signal("lo 0")
    send_signal("ls all")
       

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='LED_Controller')
    parser.add_argument('action', choices = ['on', 'off'])
    args = parser.parse_args()

    if (args.action == 'on'):
        on()

    if (args.action == 'off'):
        off()



