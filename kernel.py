#!/Users/hamid/anaconda/bin/python

#Here is the steps that I have to take
#1- I have to get the connection info file
#2- I have to get zeromq class and instansiate an object out of it
#3-I have to decod the incomming messages and send them to the kepler
#4- I have to get the results from keple nad send them back to the front end

## General Python imports:
import sys
import json
import hmac
import uuid
import errno
import hashlib
import datetime
import threading
from pprint import pformat

# zmq specific imports:
#Adding zmq liberary to the code
#This path is temperory I have to find a wayt to set it Automatically.
#import os, sys
#sys.path.append('/Users/hamid/anaconda/pkgs/pyzmq-14.3.1-py27_0/lib/python2.7/site-packages/')

import zmq
from zmq.eventloop import ioloop, zmqstream
from zmq.error import ZMQError

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


__version__ = '0.1'




if __name__ == '__main__':
    from IPython.kernel.zmq.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=MyKernel)