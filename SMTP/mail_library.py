# Matthew Maring
# CS331 Spring 2021

import smtplib

sender = "cs331@gloin.cs.colby.edu"
rcpt = "mhmari22@gloin.cs.colby.edu"
message = "Subject SMTP Test\nThis is a test by Matthew."

server = smtplib.SMTP("localhost")
server.sendmail(sender, rcpt, message)
