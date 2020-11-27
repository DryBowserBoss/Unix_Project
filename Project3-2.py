# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:21:01 2020

@author: Tyler Lenovo Flex
"""

import re

def readFile (inputFile,resultsWords,resultsNum):
    f = open(inputFile, "r")
    for line in f:
        for word in line.split(' '):
            resultsWords = 1
    return resultsWords,resultsNum;

def simplifyString (inString):
    outString = re.sub('[\W_]+','',inString)
    return outString.lower()

tester = "GYUVDYUW)((*&^^%@!$#^@bbdujsbFDIUR898_+_+_+judebufjbh"
print(simplifyString(tester))