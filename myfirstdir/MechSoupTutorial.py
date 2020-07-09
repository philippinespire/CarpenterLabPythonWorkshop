#!/usr/bin/env python3

"""
Ctf-8,oding: u end of line character is \n, one indent is 4 spaces
Created on Tue Jul  7 07:26:06 2020
Script purpose: mechanicalsoup tutorial
Version 1.0
@author: Iván Raúl López Martínez
"""

import mechanicalsoup, re, gspread #sys
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials
Debug = True
WriteOutFile = True

def StatusFinder(CurrentStatus):
    if CurrentStatus.count(' ')==4:#function to 
        SearchStr = '(\w+),\s(\w+) .+\sCurrent status: (\w+)\s(\w+)\s(\w+)\s(\w+).+\r\n'
        Result = re.search(SearchStr, CurrentStatus)# finds the search string in the file
    elif CurrentStatus.count(' ')==3:
        SearchStr = '(\w+),\s(\w+) .+Status uncertain.+\r\n'
        Result = re.search(SearchStr, CurrentStatus)
    elif CurrentStatus.count(' ')==2:
        SearchStr = '(\w+),\s(\w+) .+a species currently recognized as valid.+\r\n'
        Result = re.search(SearchStr, CurrentStatus)
    elif CurrentStatus.count(' ')==1:
        SearchStr = '(\w+),\s(\w+) .+Family uncertain.+\r\n'
        Result = re.search(SearchStr, CurrentStatus)
    elif CurrentStatus.count(' ')==0:
        SearchStr = '.+'
        Result = re.search(SearchStr, CurrentStatus)
    return CurrentStatus

#Result.group() \2\t\1\t\3 \4 \5 \6
#InFile = input('Enter the name of the google sheet with the list:')
#LastFish = input('Enter the row number of the last species:')
Family = input('Enter the name of the family:')
#OutFileName = input('Enter the full pathway and name for the file to be created: ')
Scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
Creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/ivanlopez/API_Keys/REUapplication.json', Scope)#sys.argv
Client = gspread.authorize(Creds)
Sheet = Client.open(InFile).sheet1
OutFile = open(OutFileName, 'w') #opens the outfile for writting
Rownumber = 1
SpeciesTotal = range(1,29)

Browser = mechanicalsoup.StatefulBrowser()
Browser.open("http://researcharchive.calacademy.org/research/ichthyology/catalog/fishcatmain.asp")
Browser.select_form()
Browser.get_current_form()#.print_summary()
Browser["contains"] = Family#"caesionidae"
Response = Browser.submit_selected()
Soup = BeautifulSoup(Response.text, 'html.parser')
print(Soup.get_text())



#for Num in SpeciesTotal:
'''
    if Rownumber > 1:
        Q1Character = str(Sheet.cell((Rownumber),46))#read the input cell into a string
        Q2Character = str(Sheet.cell((Rownumber),47))
        for Junk in Bad_chars: 
            Q1Character = Q1Character.replace(Junk, '')
            Q1Character = re.sub('CellR\d+C\d+', '',Q1Character)
            Q2Character = Q2Character.replace(Junk, '')
            Q2Character = re.sub('CellR\d+C\d+', '',Q2Character)
        Q1CharacterTotal = len(Q1Character)
        if Q1CharacterTotal >=1:
            Sheet.update_cell((Rownumber), 55, Q1CharacterTotal)
        Q2CharacterTotal = len(Q2Character)
        if Q2CharacterTotal >=1:
            Sheet.update_cell((Rownumber), 56, Q2CharacterTotal)
    Rownumber += 1
 '''