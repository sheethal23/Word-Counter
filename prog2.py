#!/usr/bin/python3



#packages that are needed for this program
import sys
import os
import re

#sub-routine that checks the number of arguments 
def checkArgs():
    if len(sys.argv) != 3:                                                         #checks for the number of arguments
       sys.stderr.write('Usage: ./prog2.py inFile outFile\n\n')                    #prints the error message if number of arguments are incorrect
       exit()
    else:
       return(sys.argv)                                                            #returns input and output files as tuple

#sub-routine that opens the files received as a tuple
def openFiles(files):    
    if os.path.isfile(sys.argv[1]):                                                #checks whether the file exist or not
        print('Output Values for Data: %s' % os.path.abspath(sys.argv[1]))         #print the address of the file if exists
        print('---------------------------------------------------------')
        return files                                                               #returns file objects as a tuple
    else:
        sys.stderr.write('Can\'t Open File: %s\n\n' % os.path.abspath(sys.argv[1]))#prints the error message if file doesnt exist
        exit()

#sub-routine that closes the files 
def closeFiles(fobjects):
    if os.path.isfile(sys.argv[1]):
        return fobjects 
    else:
        sys.stderr.write('Can\'t be closed: %s\n' %  os.path.abspath(sys.argv[1])) #prints the error message if file cannot be closed
        sys.stderr.write('---------------------------------------------------------')
        exit()

#sub-routine to create a list from input stream of text of file 
def createList(inFileObj):
    inFileObj = open(sys.argv[1])                                         
    text = inFileObj.read()                                                        #creates list from contents of file 
    text = re.split('\s+|-', str(text))                                            #split the list for whitespaces and "-"
    return text

'''
sub-routine to remove all non-alphabetical characters 
from input argument and put them in dictionary along
with each word frequency
'''
def createDictionary(words):
    di = { }
    words = [items.lower() for items in words]                                    #converts all content to lower case letters
    words = [re.sub(r"('[a-z])", "", word) for word in words]              
    words = sorted(re.findall(r'[a-zA-Z]+',str(words)))                           #regular expression to match all alphabetic characters
    for line in words:                                                            
        line = line.rstrip()                                                      #loop that counts the frequency of each word in 
        wds = line.split()                                                        #an argument words and stores them in a dictionary
        for w in wds:                                                             
           di[w] = di.get(w,0) + 1   
    return di                                                                     #returns the dictionary
  
#sub-routine that prints size and contents of dictionary
def printDictionary():
    p = createDictionary(createList(openFiles(checkArgs())))
    print("size = %d\n" % len(p))                                                 #prints the size of dictionary
    count = 0
    for a in p:
        count +=1
        print ('%-20s: %2d ' % ( a, p[a] ), end='' )                              #prints contents of dictionary and its frequencies
        if count==3: print(); count = 0
    closeFiles(p)
        
printDictionary()    




    

