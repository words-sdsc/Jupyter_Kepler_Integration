
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic) 
from KeplerMagicLib import Kepler_Magic

@magics_class
class KeplerMagic(Magics):
	KeplerPath     = ''
	WorkFlowPath   = ''
	TargetFilePath = ''
	
	@line_magic
	def Kepler(self,line,**kwargs):
		Wk =  Kepler_Magic()
		paramHolder = ''
		for k in kwargs:
			paramHolder += k +' = ' + kwargs[k]
		result = 1
		result = wk.runKepler(self.KeplerPath,self.WorkFlowPath,self.TargetFilePath, FirstParam = 15)
		if result:
			line = wk.readKeplerOutput()
			wk.removeKeplerOutputFile()
		else:
			line = self.KeplerPath
			#line = self.KeplerPath+"Kepler Path is not correct. Please correct it using KeplerConfig magic function"
		return line
	
	@line_magic
	def KeplerConfig(self,line,**kwargs):
		for c in kwargs:
			if c == "KeplerPath"    :
				self.KeplerPath     = kwargs[c]
			if c == "WorkFlowPath"  :
				self.WorkFlowPath   = kwargs[c]
			if c == "TargetFilePath":
				self.TargetFilePath = kwargs[c]
		#line  = "Function Config sucess. you can run your workflow"
		line = kwargs['KeplerPath']
		return line


ip = get_ipython()
ip.register_magics(KeplerMagic)
