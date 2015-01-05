'''
Basic Command to run workflow with parameter and value from commandline:

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/Desktop ~/Desktop/addMod2.kar 

Switch to redirect any display output in the workflow to a DirPath: 

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/DirPath ~/Desktop/addMod2.kar 

This command will redirect any stdout due to the command execution to ~/Desktop/exe.txt and display the output of the workflow on console: 

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/Desktop ~/Desktop/addMod2.kar | tee > ~/Desktop/exe.txt ; cat ~/Desktop/addMod2.MonitorValue.txt
'''
import os
from IPython.display import Image

class Kepler_Magic():
	TargetFilekepler = ''
	def runKepler(self,KeplerPath,WorkFlowPath,TargetFilePath,parameters):
		self.TargetFilekepler = TargetFilePath
		if os.path.isfile(str(KeplerPath)):		
			os.system(KeplerPath+' -runwf -nogui '+parameters+'-redirectgui '+TargetFilePath+' '+WorkFlowPath)
 	
 	def readKeplerOutput(self,TargetFilekepler):
 		TempRead = ''
 		if  self.TargetFilekepler != '':
	 		try:
	 			if TargetFilekepler.endswith('.txt'):
	 				FileToread = open(TargetFilekepler)
			 		for line in FileToread.readlines():
			 			TempRead += line
			 	elif TargetFilekepler.endswith('.png'):
			 		#This is iPython class, do not use it outside
			 		TempRead = Image(filename=TargetFilekepler)
		 	except IOError as e:
		 		TempRead = "Cannot open output file". format(e)
		else:
			TempRead = "File not found!!"
		return TempRead
	def removeKeplerOutputFile(self,TargetFilekepler):
		if os.path.isfile(TargetFilekepler):
			os.remove(self.TargetFilekepler)

#We do not have main function in this file,
#this line is here in case main will be added in future
if __name__ == "__mian__":main()