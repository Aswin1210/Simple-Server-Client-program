import socket
import struct
import math

UDP_IP = "localhost" #Importing IP address, port number, Buffersize
UDP_PORT = 5005
bfrSize = 1024
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

f=open('lion.jpg','rb') #Opening the File to be sent from client to server
print ("File has been Extracted")

#for user reference to find the file size
f.seek(0,2)  # moves the file pointer to the EOF
fileSize = f.tell() #gets file size
f.seek(0,0)  # moves the file pointer the the beginning of the file
print("File size : ", fileSize)
loopTimes = (fileSize / bfrSize) #Filesize is divided by buffersize (1024) to find the loopTimes
loop=math.ceil(loopTimes) #Changing loopTimes to next integer
loop_bytes = struct.pack("<i", loop) #changing loop from interger to byte
sock.sendto(loop_bytes,(UDP_IP,UDP_PORT)) #sending the file size to Server

imgFile = f.read(bfrSize) #reading the file
sock.sendto(imgFile,(UDP_IP,UDP_PORT)) #Sending the file to server

for i in range(0,loop): #it runs 'loop' times
    sock.sendto(imgFile,(UDP_IP,UDP_PORT)) #sending the file to server
    imgFile=f.read(bfrSize)
    i=i+1
f.close() #file closed
print("File Sent to Server")

'''Waiting to receive file from Server'''
print("Waiting to receive message from Server")
data, address = sock.recvfrom(1024) #Receiving the message from server
print("From Server: ", data.decode())
sock.close() #file has been received and socket has been closed
