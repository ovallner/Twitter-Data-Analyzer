#Twitter Data Analyzer
##This Twitter data analyzer is designed to be used without coding experience
To use this account analyzer, follow the instructions given below on how to set up the environment. The code is then run by passing "arguments" to a script that then takes care of everything. This analyzer DOES require at least some familiarity with terminal, however I have attempted to outline all the info needed in this README. This set-up tutorial is designed to be used in a MacOS environment, however it will work in any environment provided the user knows how to install the
required dependencies.
##Terminal Crash course
###Skip this section if you are already familiar with navigating a file system within terminal
- To open the terminal on your Mac, press <kbd>Command</kbd>+<kbd>space</kbd> and type terminal into the search box and press enter. This will open a terminal window in the directory of the current user. 
- To get a list of all files and folders in the current directory, type **ls** and press enter
- To navigate to a folder within your current directory (current folder), type **cd <Directory Name>** and replace <Directory Name> with the name of the directory you want to navigate to. For example, **cd Documents** will change the directory to Documents, provided there is a directory named Documents within the current directory. You can use **cd ..** to navigate to the directory one above the current directory. So if you used **cd Documents** to navigate to the Documents directory, you can use **cd ..** to return to the directory you were just in.
##Installation
###MongoDB
Copy and paste the following command into your terminal to install homebrew to assist with the installation of MongoDB. MongoDB is going to be the Database we are using to store the tweets we are analyzing.
- /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
Copy and paste the following commands to install MongoDB
- brew update
- brew install mongodb
###Pymongo
