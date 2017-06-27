# Twitter Data Analyzer

## This Twitter data analyzer is designed to be used without coding experience

To use this account analyzer, follow the instructions given below on how to set up the environment. The code is then run by passing "arguments" to a script that then takes care of everything. This analyzer DOES require at least some familiarity with terminal, however I have attempted to outline all the info needed in this README. This set-up tutorial is designed to be used in a MacOS environment, however it will work in any environment provided the user knows how to install the
required dependencies.

## Terminal Crash course

### Skip this section if you are already familiar with navigating a file system within terminal

- To open the terminal on your Mac, press <kbd>Command</kbd>+<kbd>space</kbd> and type terminal into the search box and press enter. This will open a terminal window in the directory of the current user. 
- To get a list of all files and folders in the current directory, type `ls` and press <kbd>enter</kbd>
- To navigate to a folder within your current directory (current folder), type `cd <Directory Name>` and replace <Directory Name> with the name of the directory you want to navigate to. For example, `cd Documents` will change the directory to Documents, provided there is a directory named Documents within the current directory. You can use `cd ..` to navigate to the directory one above the current directory. So if you used `cd Documents` to navigate to the Documents directory, you can use `cd ..` to return to the directory you were just in.

## Installation
*Please note that when I use the phrase "Copy and paste into your terminal", that also means to press enter after copy and pasting to execute the command*
### MongoDB

Copy and paste the following command into your terminal to install homebrew to assist with the installation of MongoDB. MongoDB is going to be the Database we are using to store the tweets we are analyzing.

- `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

Copy and paste the following commands to install MongoDB
- `brew update`
- `brew install mongodb`

### Python Libraries

Copy and paste the following commands into your terminal to install pip, wordcloud, and Pymongo. Pymongo is the Python Library used to connect the code with MongoDB and wordcloud is used to generate a wordcloud from the tweets
- `sudo easy_install pip`
- `sudo pip install pymongo`
- `sudo pip install wordcloud`

## Using the Data Analyzer
### Downloading the Code
To get the code from this repository, first install Git using the following command in your terminal
- `brew install git`

Now that Git is installed, you can "Clone" this repository onto your own computer to use the code. First, navigate to the directory you want the code to be in. I recommend using `cd ~/Documents` to navigate to your Documents folder, then using `mkdir <Dir_Name>` to create a new folder, replacing <Dir_Name> with the name of the folder you want to put the code in. You can then do `cd <Dir_Name>` to navigate into your new folder. You are now ready to "Clone" this repository with the
following command:
- `git clone https://github.com/ovallner/Twitter-Data-Analyzer.git`

### Running the Code
To run the code, place the folder of a Month's worth of tweets into the same folder as the code. You can do this by dragging and dropping within Finder. From here, there are several different options for running the code
##### 1 day at a time
To run the code 1 day at a time, simply copy and paste the following command into your terminal:
- `./run_day.sh mm-dd` 
where mm-dd is the month and day of the date in that format (for example 02-21 is Feb 21st)

##### Add to larger collection
If you want to add the data to a collection larger than 1 day (for example, if you wanted to analyze a whole week or a whole month) run the following command in terminal:
- `./run_day.sh mm-dd <coll_name>`
with the same date format as above, and replacing <coll_name> with the name of the collection you want to use to hold several dates. You will need to run this command with multiple dates.
Ex
- `./run_day.sh 02-03 week1`
- `./run_day.sh 02-04 week1`
- `./run_day.sh 02-05 week1`
- ...
- `./run_day.sh 02-09 week1`
This will add each date into a collection called week1. CSVs can be generated and this can be analyzed using the following 2 commands respectively:
- `./expanded_csv_generator.py week1`
- `./analysis.py week1`

This can be expanded to be as large or as small as you would like, just by changing how many individual dates you add to the same collection
