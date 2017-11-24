# Name: hashFiles.py
# Authors: Keiser, Froling, Lunderman

# Last Revision: 11/20/2017

# Desc: hash all files on an OS and output to a file that will be used with diff
 later
 # tested on: <list os's that have been added to the test list>

# imports
import hashlib
import os
import sys
import platform
from subprocess import call

# name: find_os
# desc: figures out which os is running on the computer the script is running, to know to iterate through "/" or drives (C:, etc)
# params:
# returns: windows or posix
def find_os():
        name = call(["os.name()"]) # gets the os name (for unix, "posix")
        print ("NAME: %s", name)
        if name == "posix":
                return name
        else:
                name = call[("platform.system")]
                print ("NAME2: %s", name)
                if name == "Windows":
                        return name

# name: find_windows_version
# desc: determines the version of windows that is being run on the current box
# params: NA
# returns: window version
def get_winver():
    version = ""
    wv = sys.getwindowsversion()
    ## Determine the version using windows numbering schema
    if(wv.major == 6 and wv.minor == 2):
        version = "WIN_8"
    elif(wv.major == 6 and wv.minor == 1):
        version = "WIN_7"
    elif (wv.major == 10):
        version = "WIN_10"
    return version

# name: hashFile
# Desc: hashes a file
# params: filename
# returns: a hash
def hashfile(filename):
        hashed = hashlib.md5(open(filename, 'rb').read()).hexdigest()
        close(filename)
        return hashed

# name: main
# desc: this is the main function
def main():
        ## put a function for finding out OS, to know to iterate through / or the drives (c:, etc)
        outfile = raw_input("Enter an output file path: ") #this is where the hashes go
        while not True:
                if (os.path.exists(outfile) == True): #check path existance

                        #change to that directory on local machine
                        #create and open filename for the hashes to be stored in (or text process and take last part of the output file)
                        #hashes = open(<filename>, a)

                        pass
                else:
                        outfile = raw_input("Enter an output file path: ")
        name = find_os() # return Unix or Windows

        if name == "posix":
            root_dir = "/"
        else:
            if name == "Windows":
                root_dir == "C:\"
        for root, directs, files in os.walk(root_dir, topdown=True):
                for f in files:
                ret_hash = hashfile(f)
                #hashes.write(ret_hash)    #write hash of file to the output file


if __name__ == "__main__":
        main()
