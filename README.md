# VSMrpi


#To run python file at startup as a service
sudo nano /etc/rc.local
...\..
..
..
sleep 10
sudo python3 /home/pi/folder/pfile.py &     ("&" flag will run this file as a service in Debian linux system)

right before exit(0)
