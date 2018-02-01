import socket
import struct

UDP_IP = "localhost" #Importing IP address, port number, Buffersize
UDP_PORT = 5005
bufrsize= 1024
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print("Server Started")

p = open('Received Image.jpg', 'wb') #Opening a new file where the transferred image is copied

loopTimes,address=sock.recvfrom(bufrsize) #Receiving file size from Client

loop= struct.unpack("<i", loopTimes)[0] #changing byte to integer

data, addr = sock.recvfrom(bufrsize)  # Receiving File from Client, buffer size is 1024 bytes
print ("write/Receiving process starting soon")

for i in range(0,loop): #Loop to write entire transferred image in the new file
        data, addr = sock.recvfrom(bufrsize)
        p.write(data)
        i+=1
p.close() #closing the file
print ("Image File Received") #Image Received from Client

'''Sending Message to Client'''
MESSAGE= b'File Received'
#print(f"Sending reply to CLient {address}.....") #Getting address of the client to send message
sock.sendto(MESSAGE,(address)) #message sent to Client
print("Server sent message to client: ",MESSAGE.decode())
sock.close() #Server sent message sucessfully to client and socket is closed
