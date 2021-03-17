// Matthew Maring
// CS331 Spring 2021

const net = require('net')
serverName = "localhost"
serverPort = 25
const socket = net.createConnection(serverPort, serverName)

count = 0

socket.on('data', (data) => {
	output = data.toString()
	console.log(output)
	if (count == 0 && output.substring(0, 3) == "220") {
		socket.write("helo gloin.cs.colby.edu\r\n")
		count++
	} else if (count == 1 && output.substring(0, 3) == "250") {
		socket.write("mail from: cs331@gloin.cs.colby.edu\r\n")
		count++
	} else if (count == 2 && output.substring(0, 3) == "250") {
		socket.write("rcpt to: mhmari22@gloin.cs.colby.edu\r\n")
		count++
	} else if (count == 3 && output.substring(0, 3) == "250") {
		socket.write("data\r\n")
		count++
	} else if (count == 4 && output.substring(0, 3) == "354") {
		socket.write("subject: SMTP test\nthis is a test by Matthew Maring\n.\r\n")
		count++
	} else if (count == 5 && output.substring(0, 3) == "250") {
		socket.write("quit\r\n")
		count++
	} else {
		socket.destroy()
	}
	
})