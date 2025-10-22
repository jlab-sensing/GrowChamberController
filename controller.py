import RPi.GPIO as GPIO
import serial
import argparse
from time import sleep


EN_485 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485, GPIO.OUT)
GPIO.output(EN_485, GPIO.HIGH)

t = serial.Serial("/dev/ttyS0", 9600, timeout=1)


def send_signal(input: str) -> str:
    GPIO.output(EN_485, GPIO.HIGH)
    strInput = input + "\r\n"
    t.write(strInput.encode())
    GPIO.output(EN_485, GPIO.LOW)
    ret = t.readall()
    return ret


def set_brightness(level: int):
    if level <= 0 or level >= 2000:
        raise ValueError("Brightness level must be between 0 and 2000")
    command = f"lo {level}"
    send_signal(command)
    sleep(0.2)
    send_signal("ls all")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="LED Controller")
    parser.add_argument("brightness", type=int, help="Set brightness level(0-2000)")
    args = parser.parse_args()

    print(f"Setting brightness to {args.brightness}")
    set_brightness(args.brightness)
