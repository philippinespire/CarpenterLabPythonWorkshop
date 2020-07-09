#!/usr/bin/env python3

"""
# -*- coding: utf-8 -*-
Created on Thu Jun 18 14:07:55 2020
Script purpose: The purpose of this script is to practice writting and reading files.  It will loop over a txt file to create a .kml file
The full script is in Haddock & Dunn 2011 PCFB page 196
Version 1.0
@author: Ivan
"""
#If you need to debug use the lines below
#Debug = True
#if Debug:bu
#    print(variable)
import posicon

InFileName = 'Marrus_claudanielis.txt'
InFile = open(InFileName, 'r')
InFileName = InFileName.replace('.txt','')
LineNumber = 0
WriteOutFile = True
OutFileName = InFileName + '.kml'
Header = 'Dive\tDepth\tLatitude\tLongitude\tDate\tComment'
if WriteOutFile:
    OutFile = open(OutFileName,'w')
    OutFile.write(Header)
    
for Line in InFile:
    if LineNumber >0:
        Line = Line.strip('\n')
        ElementList = Line.split('\t')
        LatDegrees = posicon.decimalat(ElementList[2])
        LonDegrees = posicon.decimalat(ElementList[3])
        OutputString = '%s\t%4s\t%10.5f\t%10.5f\t%9s\t%s' %(ElementList[0],ElementList[4],LatDegrees,LonDegrees,ElementList[1],ElementList[5])
        if WriteOutFile:
            OutFile.write(OutputString+'\n')
    LineNumber = LineNumber +1        
InFile.close()
OutFile.close()
