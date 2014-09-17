#Here is the steps that I have to take
#1- I have to get the connection info file
#2- I have to get zeromq class and instansiate an object out of it
#3-I have to decod the incomming messages and send them to the kepler
#4- I have to get the results from keple nad send them back to the front end
__version__ = '0.1'
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
import zmq
from zmq.eventloop import ioloop, zmqstream
from zmq.error import ZMQError

#Since I am building the new kernal for the new language Ihave to use the 
#the wire messaging system,for more information :
#http://ipython.org/ipython-doc/dev/development/messaging.html
#http://stackoverflow.com/questions/16240747/sending-messages-from-other-languages-to-an-ipython-kernel


class KeplerKernel(Kernel):




if __name__ == '__main__':
    from IPython.kernel.zmq.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=MyKernel)