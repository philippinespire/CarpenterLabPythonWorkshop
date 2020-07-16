#!/usr/bin/env python3

Usage = """
Ctf-8,oding: u end of line character is \n, one indent is 4 spaces
Created on Mon Jul 13 12:57:47 2020
Script purpose: FamFetcher.py. Retrieves all the species listed in a fish family from the Califorina Academy
of sciences and compiles the species into a csv file. 
Version 1.0
@author: Iván Raúl López Martínez
Usage:
	FamFetcher.py
"""

import mechanicalsoup, re, os, sys, time
from bs4 import BeautifulSoup

def StatusFinder(CurrentStatus):#fuction to find stings in CAS format txt files
    global NameStatus
    if  CurrentStatus.count(' ')==4:#Result.group() \2\t\1\t\3 \4 \5 \6 \7
        SearchStr = '(\w+),\s(\w+)\s(\w+).+\sCurrent status: (\w+)\s(\w+)\s(\w+)\s(\w+).+'
        Result = re.search(SearchStr, CurrentStatus)# finds the search string in the file
        Species = Result.group(1)#each captured result is saved to a variable
        Genus = Result.group(2)
        Author = Result.group(3)
        Validity = Result.group(4)
        Preposition = Result.group(5)
        VGenus = Result.group(6)
        VSpecies = Result.group(7)
        NameStatus = Genus + '\t' + Species + '\t' + Validity + '\s' + Preposition + '\s' + VGenus + '\s' + VSpecies + '\s' + Author
        return NameStatus
    elif CurrentStatus.count(' ')==3:
        SearchStr = '(\w+),\s(\w+)\s(\w+).+Status uncertain.+'
        Result = re.search(SearchStr, CurrentStatus)
        Species = Result.group(1)
        Genus = Result.group(2)
        Author = Result.group(3)
        Status = 'Status uncertain'
        NameStatus = Genus + '\t' + Species + '\t' + Status + '\s' + Author
        return NameStatus
    elif CurrentStatus.count(' ')==2:
        SearchStr = '(\w+),\s(\w+)\s(\w+).+species currently recognized as valid.+'
        Result = re.search(SearchStr, CurrentStatus)
        Species = Result.group(1)
        Genus = Result.group(2)
        Author = Result.group(3)
        Status = 'Species currently recognized as valid'
        NameStatus = Genus + '\t' + Species + '\t' + Status + '\s' + Author
        return NameStatus
    elif CurrentStatus.count(' ')==1:
        SearchStr = '(\w+),\s(\w+)\s(\w+).+Family uncertain.+'
        Result = re.search(SearchStr, CurrentStatus)
        Species = Result.group(1)
        Genus = Result.group(2)
        Author = Result.group(3)
        Status = 'Family uncertain'
        NameStatus = Genus + '\t' + Species + '\t' + Status + '\s' + Author
        return NameStatus
    elif CurrentStatus.count(' ')==0:
        SearchStr = '(\w+),\s(\w+)\s(\w+)\s(.+)'
        Result = re.search(SearchStr, CurrentStatus)
        Species = Result.group(1)
        Genus = Result.group(2)
        Author = Result.group(3)
        Status = Result.group(4)
        NameStatus = Genus + '\t' + Species + '\t' + Status + '\s' + Author
        return NameStatus

StartTime = time.time()
ScriptName = sys.argv[0]
LineNumber = 0
Family = input('Enter the name of the family:')# apogonidae
RawFileName = Family + 'raw.txt'
PathName = input('Enter the full pathway for the working directory: ')# /Users/ivanlopez/Desktop/test/
os.chdir(PathName)
RawFile = open(RawFileName, 'w')
Browser = mechanicalsoup.StatefulBrowser()
Browser.open("http://researcharchive.calacademy.org/research/ichthyology/catalog/fishcatmain.asp")
Browser.select_form()
Browser.get_current_form()#.print_summary()
Browser["contains"] = Family
Response = Browser.submit_selected()
Soup = BeautifulSoup(Response.text, 'html.parser')
RawFile.write(Soup.get_text())
Lines = open(RawFileName).readlines()
open(RawFileName, 'w').writelines(Lines[88:-1])

ReadFile = open(RawFileName, 'r')#Open the input file for reading
TextFileName = Family + '.txt'
TextFile = open(TextFileName, 'w')
LineNumber = 0
Stopper = 'It’s time to start exploring.'

for Line in ReadFile:
    if not len(Line.strip())==0:
        TextFile.write(Line)
        if Line == Stopper:
            TextFile.close() 
    LineNumber += 1#adds a row and loops to end

Header = 'Genus\tSpecies\tCurrent Status(Genus Species) Author'
OutcsvName = Family + '.csv'
Outcsv = open(OutcsvName, 'w')
Outcsv.write(Header + '\n')
RowNumber = 0
LastFile = open(TextFileName, 'r')

for Row in LastFile: #Loop through each line in the file
    if RowNumber > 0: #skip header
        Row = Row.strip('\n') # remove end of line
        ElementBase = Row.split()
        ElementRow = StatusFinder(ElementBase)
        OutputString = "%s" %(ElementRow)#complies the line
        Outcsv.write(OutputString+'\n')#Writes the line to the file
    LineNumber += 1#adds a row and loops to end

ReadFile.close()
LastFile.close() #close the files after the loop
Outcsv.close()
#os.remove(RawFileName)
#os.remove(TextFileName)
sys.stderr.write("I have finished this script") #: %s\n" % ScriptName)
print('Elapsed: %.5f' %(time.time() - StartTime))