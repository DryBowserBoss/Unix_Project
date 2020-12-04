# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:21:01 2020

@author: Tyler Lenovo Flex
"""

import re
import numpy as np
import sys

#Function for reading the file and changing the result arrays
#inputFile - string of file to open
#resultWords - array of words found
#resultNum - array of ints for how many times its corresponding word has shown up
def readFile (inputFile,resultWords,resultNum):
    f = open(inputFile, "r") #opens the files
    for line in f: #gets lines from file
        for word in line.split(' '): #gets words in file
            word = simplifyString(word)
            if (word != ''): #ignores empty strings
                if not word in resultWords: #if new word
                    #add word to arrays
                    resultWords = np.append(resultWords,word)
                    resultNum = np.append(resultNum,1)
                else: #if repeated word
                    loc = np.where(resultWords == word) #find array location
                    resultNum[loc[0]] = resultNum[loc[0]] + 1 #increment correct count
    return resultWords,resultNum;

#takes string and removes non-letter/number characters and converts all letters
#to lower case
def simplifyString (inString):
    outString = re.sub('[\W_]+','',inString)
    return outString.lower()

#must have an input argument for a file to read
if len(sys.argv) < 2:
    print("For proper use, please add at least one file to read from")
    print("Ex: Project3-2.py tester.txt")
else:
    #resultWords and resultNum
    rW = np.array([])
    rN = np.array([])
    for i in range(1,len(sys.argv)): #loop for all inputs given
        rW,rN = readFile(sys.argv[i], rW,rN)
    output = open("result.txt", "w") #open results.txt
    while(rW.shape[0] > 0):
        bestLoc = 0
        bestTotal = 0
        for i in range(rW.shape[0]):
            if rN[i] > bestTotal: #find the most used word
                bestLoc = i
                bestTotal = rN[i]
        output.write(rW[bestLoc] + " - " + str(int(rN[bestLoc])) + "\n") #output the most used word
        rW = np.delete(rW,[bestLoc]) #remove most used word from list
        rN = np.delete(rN,[bestLoc])
    output.close() #close output