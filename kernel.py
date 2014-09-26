#!/Users/hamid/anaconda/bin/python

#Here is the steps that I have to take
#1- I have to get the connection info file
#2- I have to get zeromq class and instansiate an object out of it
#3-I have to decod the incomming messages and send them to the kepler
#4- I have to get the results from keple nad send them back to the front end



# zmq specific imports:
#Adding zmq liberary to the code
#This path is temperory I have to find a wayt to set it Automatically.
import zmq
from zmq.eventloop import ioloop, zmqstream
from zmq.error import ZMQError

#importing json to handle messaging
import json
# general inofrmation import
from version_info import Ikepler_version

#Since I am building the new kernal for the new language Ihave to use the 
#the wire messaging system,for more information :
#http://ipython.org/ipython-doc/dev/development/messaging.html
#http://stackoverflow.com/questions/16240747/sending-messages-from-other-languages-to-an-ipython-kernel
#Smaple reqest and repley in Ipython
"""
The request:
[
  <IDS|MSG>
  6ea6b213262402cc1ad3c1d3e342a9f6
  {"date":"2013-04-27T23:22:13.522049","username":"minrk","session":"5b03b89a-93c9-4113-bb85-17ba57233711","msg_id":"c6d0f85e-fc25-4f1e-84e1-3d706b615393","msg_type":"execute_request"}
  {}
  {}
  {"user_variables":[],"code":"1\n","silent":false,"allow_stdin":true,"store_history":true,"user_expressions":{}}
]
and its reply:

[
  5b03b89a-93c9-4113-bb85-17ba57233711
  <IDS|MSG>
  47d1052f6e8f333d18480938ca91719b
  {"date":"2013-04-27T23:22:13.528239","username":"kernel","session":"d7eb303b-d2d0-4723-aef2-738545a8da11","msg_id":"9ed1d332-398c-4132-b203-1e7bf8fed712","msg_type":"execute_reply"}
  {"date":"2013-04-27T23:22:13.522049","username":"minrk","session":"5b03b89a-93c9-4113-bb85-17ba57233711","msg_id":"c6d0f85e-fc25-4f1e-84e1-3d706b615393","msg_type":"execute_request"}
  {"dependencies_met":true,"engine":"645fb29f-37ab-40c9-bc01-b7fbfe3c2112","status":"ok","started":"2013-04-27T23:22:13.524114"}
  {"status":"ok","execution_count":2,"user_variables":{},"payload":[],"user_expressions":{}}
]
"""
"""
Zeromq socket descriptions
REP: The only thing this socket does is receive requests and then reply to them.

REQ: This socket is the opposite of REP - it sends requests and reads replies to them.

PUB: This socket broadcasts (publishes) information to anyone who is listening.

SUB: This socket subscribes to a PUB socket and listens to all its broadcasts.

ROUTER: This socket can be used as a multi-user REP socket. It can receive requests 
from many other sockets and reply to all of them. ROUTER sockets store the identity 
of the source of the message before sending the message to the application, and the 
application receives messages from all origins. When replying to a message, the ROUTER 
socket will send the reply to the origin of the request.

DEALER: This socket allows round-robin communication between sets of sockets. 
If a message is sent to a DEALER, the DEALER will send to all connected peers. 
This allows sets of sockets to communicate without explicit knowledge of all the sockets in the set.
"""
# This object holds the kernel name and the version
ver  = Ikepler_version()










