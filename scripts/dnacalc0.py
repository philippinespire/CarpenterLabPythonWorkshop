#! /usr/bin/env python
'''#Usage: This script takes an input string of DNA sequence and returns the length, and percent 
composition of individual
#written by ME
'''

DNASeq = input('Enter a DNA sequence:') #this assigns user input to a variable called DNASeq

###Sanitizing###
DNASeq = DNASeq.upper().replace(' ','') #convert to uppercase for .count() function to work

print('Sequence:',DNASeq)

SeqLength = float(len(DNASeq)) #this calculates the length of a string as an integer and then converts to a floating point

print('Sequence Length:', SeqLength)

NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberT = DNASeq.count('T')
NumberG = DNASeq.count('G')

#Old way to output the Numbers
print('A: %.1f %%' %(100*NumberA/SeqLength))
print('C: %.1f %%' %(100*NumberC/SeqLength))
print('G: %.1f %%' %(100*NumberG/SeqLength))
print('T: %.1f %%' %(100*NumberT/SeqLength))