from DNAToolkit import *
from structures import *
from utilities import *
import random


randDNAStr = ''.join([random.choice(Nucleotides) 
                      for nuc in range(20)])

#rndDNAStr = "ATTCXGT"
DNAStr = validateSeq(randDNAStr)

#print(validateSeq(randDNAStr))
#print(countNucFrequency(randDNAStr))
#print(transcription(randDNAStr))
#print(reverse_complement(DNAStr))

print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] Sequence Lenght: {len(DNAStr)}\n')
print(f'[2] Nucleotide Frequency: {nucleotide_frequency(DNAStr)}\n')
print(f'[3] Transcription: {colored(transcription(DNAStr))}\n')
print(f"[4] DNA String + Reverse Complement: \n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr)[::-1])} 5' [Complement]")
print(f"5' {colored(reverse_complement(DNAStr))} 3' [Rev. Complement ]\n")

print(f'[5] GC Content: {gc_content(DNAStr)}%\n')
print(f'[6] GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')