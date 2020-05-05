#### examples from chapter 5

# save all reports in one text file:
curl "https://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=IFREESTA28&day=[01-31]&month=12&year=2017&graphspan=day&format=1" >> Ifreestationweather.txt

# save each month's report in its own numbered file 
curl "https://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=IFREESTA28&day=[01-31]&month=12&year=2017&graphspan=day&format=1" -o Ifreestation_2017-12-#1.txt

# save specific files with original names
# Mac
curl "http://files.rcsb.org/view/{1ema,1gfl,1g7k,1xmz}.pdb" -o #1.pdb
# Windows git bash
curl "http://files.rcsb.org/view/{1ema,1gfl,1g7k,1xmz}.pdb" -O

#### examples from chapter 6

# the lines to set your path in ~/.bash_profile or ~/.zshrc
#Windows git bash and mac terminal bash
.bash_profile
#Ubuntu
.bashrc
#Mac zsh
.zshrc

export PATH="$PATH:$HOME/scripts"
set -o noclobber

# general crossref search format
http://www.crossref.org/openurl/?title=Nature&date=2008&volume=452&spage=745&pid=demo@practicalcomputing.org

#  crossref search format returning XML
http://www.crossref.org/openurl/?title=Nature&date=2008&volume=452&spage=745&pid=demo@practicalcomputing.org&redirect=false&format=unixref

# reformatted for a regular expression
curl "http://www.crossref.org/openurl/?title=\1\&date=\2\&volume=\3\&spage=\4\&pid=demo@practicalcomputing.org\&redirect=false\&format=unixref" 

