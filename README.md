#ipython kepler integration

[Kepler Project page](https://kepler-project.org/) |
[SDSU Words Group](http://words.sdsc.edu/) |
[ipython website](http://ipython.org/) |

This app will integrate kepler workflows with ipython notebooks.

#Installation 
* Install [Kepler] (https://kepler-project.org/) (if you already have it installed on your machine skip this step).
* Install [ipython](http://ipython.org/install.html) 
* Download this [package] (https://github.com/hamidre13/IPython-Kepler-Magic-Function/archive/master.zip)
* Extract it, and got the the extracted folder
* From command line Run : python setup.py install

#Instructions

* First Import KeplerMagic
* Set the location of kepler.sh : %KpConf path to kepler.sh (You need to run this command only one time!)
* Set workFlow Path: %WpConf WorkFlowPath
* Run workflow with any parameters: %Kepler parameters
* Read the output to the notebook: %readoutput output file name


