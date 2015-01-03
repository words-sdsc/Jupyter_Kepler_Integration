'''
Basic Command to run workflow with parameter and value from commandline:

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/Desktop ~/Desktop/addMod2.kar 

Switch to redirect any display output in the workflow to a DirPath: 

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/DirPath ~/Desktop/addMod2.kar 

This command will redirect any stdout due to the command execution to ~/Desktop/exe.txt and display the output of the workflow on console: 

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/Desktop ~/Desktop/addMod2.kar | tee > ~/Desktop/exe.txt ; cat ~/Desktop/addMod2.MonitorValue.txt

2- I have to set the flag for the users to be able to change the path
3- I have to use try catch so if I get permission denied I will be able to change the file permision then run the app again 
'''
import platform
import os
import subprocess 

class Kepler_Magic():
	def runKepler(self,KeplerPath,WorkFlowPath,TargetFilePath,**kwargs):
		TempArgumentHolder =''
		for KeplerParam in kwargs:
			TempArgumentHolder += '-'+KeplerParam+' '+str(kwargs[KeplerParam])+' '
		if os.path.isfile(KeplerPath):		
			os.system(KeplerPath+' -runwf -nogui '+TempArgumentHolder+'-redirectgui '+TargetFilePath+' '+WorkFlowPath)
		else:
			return 0
 	def readKeplerOutput(self):
 		TempRead = ''
 		try:
 			FileToread = open('/Users/hamid/Desktop/simpleadd.Display.txt')
	 		for line in FileToread.readlines():
	 			TempRead += line
	 	except IOError as e:
	 		TempRead = "Cannot open output file". format(e)
		
		return TempRead
	def removeKeplerOutputFile(self):
		if os.path.isfile('/Users/hamid/Desktop/simpleadd.Display.txt'):
			os.remove('/Users/hamid/Desktop/simpleadd.Display.txt')

#We do not have main function in this file,
#this line is here in case main will be added in future
if __name__ == "__mian__":main()