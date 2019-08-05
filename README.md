#Jupyter kepler integration

[Kepler Project page](https://kepler-project.org/) |
[SDSC Words Group](http://words.sdsc.edu/) |
[ipython website](http://ipython.org/) |

This app will integrate kepler workflows with Jupyter notebooks.

#Installation 
* Install [Kepler] (https://kepler-project.org/) (if you already have it installed on your machine skip this step).
* Install [ipython](http://ipython.org/install.html) 
* Download this [package] (https://github.com/hamidre13/IPython-Kepler-Magic-Function/archive/master.zip)
* Extract it, and go to the extracted folder
* From command line Run : python setup.py install

#Instructions

These functions will be standardized in future releases 
* First import KeplerMagicFunction
* Set the location of kepler.sh : %KpConf path to kepler.sh (You need to run this command only one time!)
* Set workFlow Path: %WpConf WorkFlowPath
* Run workflow with any parameters: %Kepler parameters
* Read the output to the notebook: %readoutput output file name


