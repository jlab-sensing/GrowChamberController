# GrowChamberController

## Usage

```
$ python controller.py --help
usage: LED Controller [-h] brightness

positional arguments:
  brightness  Set brightness level(0-2000)

options:
  -h, --help  show this help message and exit
```

## Setup RS485

Follow the instructions to setup the RS485 hat for the raspberry pi.

https://www.waveshare.com/wiki/RS485_CAN_HAT#RS485_Usage

## Install controller

First ensure you can ssh into the device without providing a password.

```bash
ssh tyler@172.31.100.200
```

Then you can install the grow chamber controller with the following ansible script

```bash
ansible-playbook -i inventory.yaml install.yaml
```
