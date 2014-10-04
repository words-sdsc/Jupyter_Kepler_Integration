#!/Users/Nick/anaconda/lib/python2.7
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
def load_ipython_extension(ipython):
    # The `ipython` argument is the currently active `InteractiveShell`
    # instance, which can be used in any way. This allows you to register
    # new magics or aliases, for example.

def unload_ipython_extension(ipython):
    # If you want your extension to be unloadable, put that logic here.