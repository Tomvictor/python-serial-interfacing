import time
import serial


ser = serial.Serial(
  
   port='/dev/tty.usbmodemL50000D1',
   baudrate = 115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
counter=0


while 1:
   x=ser.readline()
   print x