import os, sys
from fcntl import ioctl
from ioctl_cmds import *

global data 
data = 0x00;
global data1
data1 = 0xFFFFFFFF;
global data2
data2 = 0xFFFFFFFF;

def main():
    fd = os.open("/dev/mydev", os.O_RDWR)
    #while True:
        #ligar_leds(fd)
    controlar_display(fd)    
    controlar_leds_verde(fd)
    monitorar_button(fd)
    os.close(fd)

def controlar_leds_verde(fd):
    ioctl(fd, WR_GREEN_LEDS)
    red = os.write(fd, data.to_bytes(4, 'little'))

def pegar_switches(fd):
    ioctl(fd, RD_SWITCHES)
    red = os.read(fd, 1); # read 4 bytes and store in red var
    print("Switches 0x%X"%int.from_bytes(red, 'little'))
    return int.from_bytes(red, 'little')

def pegar_buttons(fd):
    ioctl(fd, RD_PBUTTONS)
    red = os.read(fd, 4); # read 4 bytes and store in red var
    print("Button 0x%X"%int.from_bytes(red, 'little'))
    return red

def ligar_leds(fd):
    data = pegar_switches(fd);
    ioctl(fd, WR_RED_LEDS)
    red = os.write(fd, data.to_bytes(4, 'little'))
    print("leds_v %d bytes"%red)
    print(data.to_bytes(4, 'little'))

def monitorar_button(fd):
    while True:
        ligar_leds(fd)
        if pegar_buttons(fd) == 7:
            return pegar_switches(fd)

def controlar_display(fd):
    ioctl(fd, WR_R_DISPLAY)
    red = os.write(fd, data1.to_bytes(4, 'little'))
    print("Display_L %d bytes"%red)
    ioctl(fd, WR_L_DISPLAY)
    red = os.write(fd, data2.to_bytes(4, 'little'))
    print("Display_R %d bytes"%red)

if __name__== "__main__" :
    main()
