import serial
import time


comPort = serial.Serial('COM4', 9600)
print("ComPort Initialized....")


while True:
    bytesBuffer = comPort.read(20)
    print(bytesBuffer)
    comPort.flush()
    time.sleep(0.3)
