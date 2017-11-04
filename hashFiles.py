# Name: hashFiles.py
# Authors: Keiser, Froling, Lunderman
# Last Revision: 11/03/2017
# Desc: hash all files on an OS and output to a file that will be used with diff
 later

# imports
import hashlib
import os
import sys

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
                        pass
                else:
                        outfile = raw_input("Enter an output file path: ")
        for root, directs, files in os.walk():
                for f in files:
                ret_hash = hashfile(f)
if __name__ == "__main__":
        main()
