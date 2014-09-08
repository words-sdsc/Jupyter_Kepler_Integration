#I am using the https://github.com/ivanov/vim-ipython as an exmple of connecting to the ipythone kernal
import socket 

HOST = "127.0.0.1"
port = ""
stdin_port= 49927
control_port=49928 
hb_port= 49929 
signature_scheme ="hmac-sha256" 
key = "ee5b307c-86a8-4907-8ae2-dd62f9721b08" 
shell_port =49925 
transport = "tcp" 
iopub_port =49926
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,8888))
while True:
	
	message = raw_input("Your Message: ") 
	s.send(message)
s.close();