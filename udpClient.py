import socket
import sys
import time
import serial
if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
    ip = sys.argv[1]
    port = int(sys.argv[2])
    #ip = '192.168.1.55'
    #port = 5000
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
    exit(1)
arduino = serial.Serial('COM8', 9600)
# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("Do Ctrl+c to exit the program !!")
# Let's send data through UDP protocol
while True:
    send_data = "Data from client side.....\r\n"
    s.sendto(send_data.encode('utf-8'), (ip, port))
    print("\n 1. Client Sent : ", send_data, "\n")
    data, address = s.recvfrom(5000)
    decoded = data.decode('utf-8')
    arr = bytearray(decoded,'utf-8')
    print("\n 2 Client received : ", decoded, "\n")
    arduino.write(arr)
    arduino.write("\n".encode())
    arduino.flush()
    time.sleep(0.5)
# close the socket
s.close()
#.................................Karaar...........................
#close internet
#..ramp................................Hello friends...............
#
# Do you know who I am? I'm a Don, Don for don't in the end we all are Don. I'm the optimistic man and very well known as the giant of this media organizer.
# I'm here for peaceful agreement of the legislation... And for the act we have right now in our minds.
