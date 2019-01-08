import socket

if __name__=='__main__': 
	filename =""

	conn_info=('192.168.99.1', 9032)
	client = socket.socket()
	client.connect(conn_info)
	cmd = 'get '+filename

	client.send(cmd.encode()) 
	server_response = client.recv(1024)

	# get file size
	file_total_size = int(server_response.decode())

	# receive file
	client.send(b"ready to recv file") 
	received_size = 0  

	f = open(filename, "wb") 
	data = client.recv(4096)
	while data:
		f.write(data) 
		data = client.recv(size)
	f.close() 