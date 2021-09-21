# function to count total size in python_practice folder
# practice on mac , there might be differences for window or Linux operating system
import os

def sizeOfPythonPracticeFolder():
    for fileName in os.listdir('/usr/local/bin/python3.9 /Users/AMGA/Desktop/python_practice'):
        print('TODO')    #TODO


"""
    for fileName in os.listdir('/usr/local/bin/python3.9 /Users/AMGA/Desktop/python_practice'):
        if not os.path.isfile(os.path.join('/usr/local/bin/python3.9 /Users/AMGA/Desktop/python_practice',fileName)):
            continue
        totalsize = totalsize + os.path.getsize(os.path.join('/usr/local/bin/python3.9 /Users/AMGA/Desktop/python_practice',fileName))
        print(totalsize)
"""