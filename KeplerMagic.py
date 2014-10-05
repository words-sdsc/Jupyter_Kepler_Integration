#!/Users/hamid/anaconda/bin/python
# myextension.py


'''

	So if that sounds good, I would actually start by just writing a library.
	a Python library that makes a kepler.sh call, and tracks the filesystem outputs, 
	and embeds the appropriate ones in IPython notebook output
	then, if you want, you can wrap your Python library call in a magic to make it a bit more convenient.
 	That's all magics are for - making Python library calls more convenient. They don't have any special privileges or functionality
'''
'''
	Basic Command to run workflow with parameter and value from commandline:

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/Desktop ~/Desktop/addMod2.kar 

Switch to redirect any display output in the workflow to a DirPath: 

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/DirPath ~/Desktop/addMod2.kar 


This command will redirect any stdout due to the command execution to ~/Desktop/exe.txt and display the output of the workflow on console: 

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/Desktop ~/Desktop/addMod2.kar | tee > ~/Desktop/exe.txt ; cat ~/Desktop/addMod2.MonitorValue.txt
'''


'''
1- I have to get the kepler path based on operating system and set it to default
2- I have to set the flag for the users to be able to change the path
3- I have to use try catch so if I get permission denied I will be able to change the file permision then run the app again
4- Then I will be ready to pass the parameters and values to the 
'''
import platform
import os
import subprocess 

class Kepler_Magic():
	_PreKeplerPath = ''
	_KeplerPath = 'Kepler-2.4/Kepler.app/Contents/Resources/Java/kepler.sh'

	def __init__(self):
		
		if self.whichos() == 'Darwin':
			print('correct')
			_PreKeplerPath = '$HOME/../../Applications/'
			for root,dirs,files in os.walk('$HOME'):
				print(root)
				print(dirs)
				print(files)
		
		
	def whichos(self):
		return platform.system()

	def SetKeplerPath(self,path):
		_KeplerPath = path
		
	def runkepler(self):
		print('')
		#print(subprocess.check_output([self._KeplerPath]))


test =  Kepler_Magic()

test.runkepler()