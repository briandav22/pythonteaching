#typically when working on a project you are going to be looking to seperate as much of the code into different files and folders as possible. 
#this will ultimately make things much clearner to work on. 
#It's a hard concept to get your arms around at first, but as you use python and other languages more, you will see why it's really necessary to do this for organizational purposes.


# lets look at this program below. First notice the code structure in the vscode editor. app.py is your main function and there is a folder that holds additional things. 


#here we import the helper function we stored in a seperate folder
from helpers.my_helpers import this_is_a_helper

#here we run it. 
this_is_a_helper()