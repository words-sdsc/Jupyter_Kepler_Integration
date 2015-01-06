
'''
If we want only one function with different parameters, we have to use  argparse
'''
import argparse
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic) 
from KeplerMagicLib import Kepler_Magic

@magics_class
class KeplerMagic(Magics):
	KeplerPath     = ''
	WorkFlowPath   = ''
	TargetFilePath = ''
	wk =  Kepler_Magic()
	@line_magic
	def Kepler(self,line):
		if self.KeplerPath =='':
			if os.path.isfile('kppath.txt'):
				fh = open('kppath.txt','r')
				self.KeplerPath  = fh.readline()
		
		paramHolder = str(line)
		
		if os.path.isfile(self.WorkFlowPath):
			if os.path.isfile(self.KeplerPath):
				self.wk.runKepler(self.KeplerPath,self.WorkFlowPath,self.TargetFilePath, paramHolder)
			else:
				return "Please specify Kepler path with KpConf kepler path"
		else:
			return "Please specify workflwo path with WpConf workflwo path"
	
	@line_magic
	def readoutput(self,line):
		result = self.wk.readKeplerOutput(self.TargetFilePath+'/'+line)
		#It seems it has a problem with removing the output file!!
		#self.wk.removeKeplerOutputFile(self.TargetFilePath+'/'+line)
		return result
	@line_magic
	def KpConf(self,line):
		if line :
			try:
				fh =  open('kppath.txt','w+')
				fh.truncate()
				fh.write(line)
				fh.close()
			except IOError as e:
				Error =  "Cannot creat/open kepler path file"
			self.KeplerPath = line

	@line_magic
	def WpConf(self,line):	
		if line:
			if self.TargetFilePath == '':
				self.TargetFilePath =  os.path.dirname(os.path.realpath(line))
			self.WorkFlowPath = line

	@line_magic
	def TgConf(self,line):
		if line:
			self.TargetFilePath = line

ip = get_ipython()
ip.register_magics(KeplerMagic)
