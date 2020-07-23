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

def AuthorCorrector(AuthorGroup):
    AuthorStr = 'BÃ'
    AuthorResult = re.search(AuthorStr, AuthorGroup)
    if AuthorResult:
        AuthorName = 'Böhlke'
        return AuthorName
    else:
        AuthorStr = 'RÃ¼ppell'
        AuthorResult = re.search(AuthorStr, AuthorGroup)
        if AuthorResult:
            AuthorName = 'Rüppell'
            return AuthorName
        else:
            AuthorStr = 'GÃ¼nther'
            AuthorResult = re.search(AuthorStr, AuthorGroup)
            if AuthorResult:
                AuthorName = 'Günther'
                return AuthorName
            else:
                AuthorStr = 'ThiolliÃ'
                AuthorResult = re.search(AuthorStr, AuthorGroup)
                if AuthorResult:
                    AuthorName = 'Thiollière'
                    return AuthorName
                else:
                    AuthorStr = 'LacepÃ'
                    AuthorResult = re.search(AuthorStr, AuthorGroup)
                    if AuthorResult:
                        AuthorName = 'Lacepède'
                        return AuthorName
                    else:
                        AuthorStr = 'ForsskÃ¥l'
                        AuthorResult = re.search(AuthorStr, AuthorGroup)
                        if AuthorResult:
                            AuthorName = 'Forsskål'
                            return AuthorName
                        else:
                            AuthorStr = 'DÃ'
                            AuthorResult = re.search(AuthorStr, AuthorGroup)
                            if AuthorResult:
                                AuthorName = 'Döderlein'
                                return AuthorName
                            else:
                                AuthorStr = 'LiÃ©nard'
                                AuthorResult = re.search(AuthorStr, AuthorGroup)
                                if AuthorResult:
                                    AuthorName = 'Liénard'
                                    return AuthorName
                                else:
                                    AuthorStr = 'QuÃ©ro'
                                    AuthorResult = re.search(AuthorStr, AuthorGroup)
                                    if AuthorResult:
                                        AuthorName = 'Quéro'
                                        return AuthorName
                                    else:
                                        AuthorStr = 'MÃ¼ller'
                                        AuthorResult = re.search(AuthorStr, AuthorGroup)
                                        if AuthorResult:
                                            AuthorName = 'Müller'
                                            return AuthorName
                                        else:
                                            AuthorStr = 'LÃ'
                                            AuthorResult = re.search(AuthorStr, AuthorGroup)
                                            if AuthorResult:
                                                AuthorName = 'Lönnberg'
                                                return AuthorName
                                            else:
                                                AuthorStr = 'LarraÃ'
                                                AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                if AuthorResult:
                                                    AuthorName = 'Larrañaga'
                                                    return AuthorName
                                                else:
                                                    AuthorStr = 'KrÃ'
                                                    AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                    if AuthorResult:
                                                        AuthorName = 'Krøyer'
                                                        return AuthorName
                                                    else:
                                                        AuthorStr = 'GourÃ'
                                                        AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                        if AuthorResult:
                                                            AuthorName = 'Gourène'
                                                            return AuthorName
                                                        else:
                                                            AuthorStr = 'SchreitmÃ'
                                                            AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                            if AuthorResult:
                                                                AuthorName = 'Schreitmüller'
                                                                return AuthorName
                                                            else:
                                                                AuthorStr = 'HankÃ'
                                                                AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                if AuthorResult:
                                                                    AuthorName = 'Hankó'
                                                                    return AuthorName
                                                                else:
                                                                    AuthorStr = 'GÃ¼ldenstÃ'
                                                                    AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                    if AuthorResult:
                                                                        AuthorName = 'Güldenstädt'
                                                                        return AuthorName
                                                                    else:
                                                                        AuthorStr = 'HoÃ'
                                                                        AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                        if AuthorResult:
                                                                            AuthorName = 'Hoàng'
                                                                            return AuthorName
                                                                        else:
                                                                            AuthorStr = 'BrÃ¼ning'
                                                                            AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                            if AuthorResult:
                                                                                AuthorName = 'Brüning'
                                                                                return AuthorName
                                                                            else:
                                                                                AuthorStr = 'MÃ¤Ã¤r'
                                                                                AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                                if AuthorResult:
                                                                                    AuthorName = 'Määr'
                                                                                    return AuthorName
                                                                                else:
                                                                                    AuthorStr = 'BÄnÄrescu'
                                                                                    AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                                    if AuthorResult:
                                                                                        AuthorName = 'Bănărescu'
                                                                                        return AuthorName
                                                                                    else:
                                                                                        AuthorStr = 'KÃ'
                                                                                        AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                                        if AuthorResult:
                                                                                            AuthorName = 'Küçük'
                                                                                            return AuthorName
                                                                                        else:
                                                                                            AuthorStr = 'AlmaÃ'
                                                                                            AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                                            if AuthorResult:
                                                                                                AuthorName = 'Almaça'
                                                                                                return AuthorName
                                                                                            else:
                                                                                                AuthorStr = 'EstÃ'
                                                                                                AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                                                if AuthorResult:
                                                                                                    AuthorName = 'Estève'
                                                                                                    return AuthorName
                                                                                                else:
                                                                                                    AuthorStr = 'TsÃ'
                                                                                                    AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                                                    if AuthorResult:
                                                                                                        AuthorName = 'Tsü'
                                                                                                        return AuthorName
                                                                                                    else:
                                                                                                        AuthorStr = 'SchÃ¤fer'
                                                                                                        AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                                                        if AuthorResult:
                                                                                                            AuthorName = 'Schäfer'
                                                                                                            return AuthorName
                                                                                                        else:
                                                                                                            AuthorStr = 'GuimarÃ£es'
                                                                                                            AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                                                            if AuthorResult:
                                                                                                                AuthorName = 'Guimarães'
                                                                                                                return AuthorName
                                                                                                            else:
                                                                                                                AuthorStr = 'GÃ¼Ã'
                                                                                                                AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                                                                if AuthorResult:
                                                                                                                    AuthorName = 'Güçlü'
                                                                                                                    return AuthorName
                                                                                                                else:
                                                                                                                    AuthorStr = 'KotlÃ'
                                                                                                                    AuthorResult = re.search(AuthorStr, AuthorGroup)
                                                                                                                    if AuthorResult:
                                                                                                                        AuthorName = 'Kotlík'
                                                                                                                        return AuthorName
                                                                                                                    else:
                                                                                                                        AuthorName = AuthorGroup
                                                                                                                        return AuthorName

def StatusFinder(CurrentStatus):#fuction to find stings in CAS format txt files
    SearchStr = '^([a-z]+), ([A-Z][a-z]+)[A-z\s\.\(\)]*? ([A-Z])(.*?)([A-z\s]*) \[?.+Current status: (\w+) (\w+) (\w+) (\w+).+'
    Result = re.search(SearchStr, CurrentStatus)
    if Result:
        Species = Result.group(1)#each captured result is saved to a variable
        Genus = Result.group(2)
        RawAuthor = Result.group(3) + Result.group(4) + Result.group(5)
        Author = AuthorCorrector(RawAuthor)
        Validity = Result.group(6)
        Preposition = Result.group(7)
        VGenus = Result.group(8)
        VSpecies = Result.group(9)
        NameStatus = Genus + '\t' + Species + '\t' + Validity + ' ' + Preposition + ' ' + VGenus + ' ' + VSpecies + '\t' + Author
        return NameStatus
    else:
        SearchStr = '^([a-z]+), ([A-Z][a-z]+)[A-z\s\.\(\)]*? ([A-Z])(.*?)([A-z\s]*) \[?.+Status uncertain.+'
        Result = re.search(SearchStr, CurrentStatus)
        if Result:
            Species = Result.group(1)
            Genus = Result.group(2)
            RawAuthor = Result.group(3) + Result.group(4) + Result.group(5)
            Author = AuthorCorrector(RawAuthor)
            Status = 'Status uncertain'
            NameStatus = Genus + '\t' + Species + '\t' + Status + '\t' + Author
            return NameStatus
        else:
            SearchStr = '^([a-z]+), ([A-Z][a-z]+)[A-z\s\.\(\)]*? ([A-Z])(.*?)([A-z\s]*) \[?.+species currently recognized as valid.+'
            Result = re.search(SearchStr, CurrentStatus)
            if Result:
                Species = Result.group(1)
                Genus = Result.group(2)
                RawAuthor = Result.group(3) + Result.group(4) + Result.group(5)
                Author = AuthorCorrector(RawAuthor)
                Status = 'Species currently recognized as valid'
                NameStatus = Genus + '\t' + Species + '\t' + Status + '\t' + Author
                return NameStatus
            else:
                SearchStr = '^([a-z]+), ([A-Z][a-z]+)[A-z\s\.\(\)]*? ([A-Z])(.*?)([A-z\s]*) \[?.+Family uncertain.+'
                Result = re.search(SearchStr, CurrentStatus)
                if Result:
                    Species = Result.group(1)
                    Genus = Result.group(2)
                    RawAuthor = Result.group(3) + Result.group(4) + Result.group(5)
                    Author = AuthorCorrector(RawAuthor)
                    Status = 'Family uncertain'
                    NameStatus = Genus + '\t' + Species + '\t' + Status + '\t' + Author
                    return NameStatus
                else:
                    SearchStr = '^([a-z]+), ([A-Z][a-z]+)[A-z\s\.\(\)]*? ([A-Z])(.*?)([A-z\s]*) \[?.+Incertae sedis.+'
                    Result = re.search(SearchStr, CurrentStatus)
                    if Result:
                        Species = Result.group(1)
                        Genus = Result.group(2)
                        RawAuthor = Result.group(3) + Result.group(4) + Result.group(5)
                        Author = AuthorCorrector(RawAuthor)
                        Status = 'Incertae sedis'
                        NameStatus = Genus + '\t' + Species + '\t' + Status + '\t' + Author
                        return NameStatus
                    else:
                        SearchStr = '^([a-z]+), ([A-Z][a-z]+)[A-z\s\.\(\)]*? ([A-Z])(.*?)([A-z\s]*) \[?(.+)'
                        Result = re.search(SearchStr, CurrentStatus)
                        if Result:
                            Species = Result.group(1)
                            Genus = Result.group(2)
                            RawAuthor = Result.group(3) + Result.group(4) + Result.group(5)
                            Author = AuthorCorrector(RawAuthor)
                            Status = Result.group(6)
                            NameStatus = Genus + '\t' + Species + '\t' + Status + '\t' + Author
                            return NameStatus
                        else:
                            CurrentStatus = "It’s time to start exploring."
                            return CurrentStatus

ScriptName = sys.argv[0]
LineNumber = 0
Family = input('Enter the name of the family:')# apogonidae
PathName = input('Enter the full pathway for the working directory: ')# /Users/ivanlopez/Desktop/test/
StartTime = time.time()
os.chdir(PathName)
RawFileName = Family + 'raw.txt'
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
open(RawFileName, 'w').writelines(Lines[87:-1])

Header = 'Genus\tSpecies\tCurrent Status(Genus Species)\tAuthor'
OutcsvName = Family + '.csv'
Outcsv = open(OutcsvName, 'w')
Outcsv.write(Header + '\n')
RowNumber = 0

with open(RawFileName, mode= 'r') as LastFile:
    for Row in LastFile: #Loop through each line in the file
        if not len(Row.strip())==0:
            Row = Row.strip('\n')# remove end of line
            ElementRow = StatusFinder(Row)# applies the defined function
            if ElementRow == "It’s time to start exploring.":
                break
            Outcsv.write(ElementRow + '\n')#Writes the line to the file
            RowNumber += 1#adds a row and loops to end

Outcsv.close()
os.remove(RawFileName)# removes intermediate files
sys.stderr.write("I have finished this script: %s\n" % ScriptName)
print('Elapsed: %.5f' %(time.time() - StartTime))
"""
Script improvements:
fexibility to interface between command line and input to define variables
Option or ability to read family names from a file
"""