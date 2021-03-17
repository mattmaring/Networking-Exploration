# Matthew Maring
# CS331 Spring 2021

from socket import *
serverName = "localhost"
serverPort = 25
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage)
clientSocket.send("helo gloin.cs.colby.edu\r\n")
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage)
clientSocket.send("mail from: cs331@gloin.cs.colby.edu\r\n")
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage)
clientSocket.send("rcpt to: mhmari22@gloin.cs.colby.edu\r\n")
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage)
clientSocket.send("data\r\n")
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage)
clientSocket.send("subject: SMTP test\nthis is a test by Matthew Maring\n.\r\n")
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage)
clientSocket.close()