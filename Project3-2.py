# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:21:01 2020

@author: Tyler Lenovo Flex
"""

import re
import numpy as np
import sys

def readFile (inputFile,resultWords,resultNum):
    f = open(inputFile, "r")
    for line in f:
        for word in line.split(' '):
            word = simplifyString(word)
            if (word != ''):
                if not word in resultWords:
                    resultWords = np.append(resultWords,word)
                    resultNum = np.append(resultNum,1)
                else:
                    loc = np.where(resultWords == word)
                    resultNum[loc[0]] = resultNum[loc[0]] + 1
    return resultWords,resultNum;

def simplifyString (inString):
    outString = re.sub('[\W_]+','',inString)
    return outString.lower()

if len(sys.argv) < 2:
    print("For proper use, please add at least one file to read from")
    print("Ex: Project3-2.py tester.txt")
else:
    rW = np.array([])
    rN = np.array([])
    for i in range(1,len(sys.argv)):
        rW,rN = readFile(sys.argv[i], rW,rN)
    output = open("result.txt", "w")
    while(rW.shape[0] > 0):
        bestLoc = 0
        bestTotal = 0
        for i in range(rW.shape[0]):
            if rN[i] > bestTotal:
                bestLoc = i
                bestTotal = rN[i]
        output.write(rW[bestLoc] + " - " + str(int(rN[bestLoc])) + "\n")
        rW = np.delete(rW,[bestLoc])
        rN = np.delete(rN,[bestLoc])
    output.close()