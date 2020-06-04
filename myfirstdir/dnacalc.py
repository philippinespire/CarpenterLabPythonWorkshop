#! /usr/bin/env python

DNASeq = input('Enter a DNA Sequence: ')
#DNASeq = "ATGAAC"
DNASeq = DNASeq.upper().replace(' ','')

print ('Sequence:', DNASeq )

SeqLength = float(len(DNASeq))

print ("Sequence Length:", SeqLength)

NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT = DNASeq.count('T')

print ("A: %.2f" %(NumberA/SeqLength))
print ("C: %.2f" %(NumberC/SeqLength))
print ("G: %.2f" %(NumberG/SeqLength))
print ("T: %.2f" %(NumberT/SeqLength))


pctA  = "%.2f" %(100*NumberA/SeqLength)
pctC  = "%.2f" %(100*NumberC/SeqLength)
pctG  = "%.2f" %(100*NumberG/SeqLength)
pctT  = "%.2f" %(100*NumberT/SeqLength)

print('%A: ', pctA)
print('%C: ', pctC)
print('%G: ', pctG)
print('%T: ', pctT)

print ('A:', NumberA/SeqLength) #The book has this as an example
print ('A: %.1f %%' %(100*NumberA/SeqLength))
print ('C: %.1f %%' %(100*NumberC/SeqLength))
print ('T: %.1f %%' %(100*NumberT/SeqLength))
print ('G: %.1f %%' %(100*NumberG/SeqLength))