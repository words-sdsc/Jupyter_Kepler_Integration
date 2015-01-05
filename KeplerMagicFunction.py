
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
		paramHolder = str(line)
		result = 1
		self.wk.runKepler(self.KeplerPath,self.WorkFlowPath,self.TargetFilePath, paramHolder)
	
	@line_magic
	def readoutput(self,line):
		result = self.wk.readKeplerOutput(self.TargetFilePath+line)
		#self.wk.removeKeplerOutputFile(self.TargetFilePath+line)
		return result
	@line_magic
	def KeplerPathConfig(self,line):
		if line :
			self.KeplerPath = line

	@line_magic
	def WkPathConfig(self,line):	
		if line:
			self.WorkFlowPath = line

	@line_magic
	def TgPathConfig(self,line):
		if line:
			self.TargetFilePath = line

ip = get_ipython()
ip.register_magics(KeplerMagic)
