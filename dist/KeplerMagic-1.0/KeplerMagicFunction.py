

from IPython.core.magic import (register_line_magic, register_cell_magic,
                                register_line_cell_magic)

from KeplerMagicLib import Kepler_Magic

@register_line_magic
def lineKeplerCall(line,**kwargs):
	test =  Kepler_Magic()
	paramHolder = ''
	for k in kwargs:
		paramHolder += k +' = ' + kwargs[k]


	test.runKepler(test._PreKeplerPath,test._KeplerPath,test._WorkFlowPath,test._TargetFilePath, FirstParam = 15)
	line = test.readKeplerOutput()
	test.removeKeplerOutputFile()
	return line
