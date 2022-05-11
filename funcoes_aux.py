import os, sys
from fcntl import ioctl
from ioctl_cmds import *

if len(sys.argv) < 2:
    print("Error: expected more command line arguments")
    print("Syntax: %s </dev/device_file>"%sys.argv[0])
    exit(1)

fd = os.open(sys.argv[1], os.O_RDWR)

def pegar_switches():
    ioctl(fd, RD_SWITCHES)
    red = os.read(fd, 1); # read 4 bytes and store in red var
    print("red 0x%X"%int.from_bytes(red, 'little'))
    return red

def pegar_buttons():
    ioctl(fd, RD_PBUTTONS)
    red = os.read(fd, 4); # read 4 bytes and store in red var
    print("red 0x%X"%int.from_bytes(red, 'little'))
    return red



os.close(fd)