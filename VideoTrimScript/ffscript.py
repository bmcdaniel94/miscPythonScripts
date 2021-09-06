# ffscript.py
# Video Trimming Script
# Written by: Benjamin McDaniel

import os

#read in file location with user input
file_path=input("Location of video to trim: ")

#read in start time
starttime=input("Start time of the clip: ")
#read in end time
endtime=input("End time of the clip: ")
#ask user the name of new file
nFilename=input("Input name of new file: ")

#def ffmpeg command
ffCmd="ffmpeg -i "+file_path+" -ss "+starttime+" -to "+endtime+" -c:v copy -c:a copy "+nFilename  
#pass ffmpeg command through terminal
os.system(ffCmd)
