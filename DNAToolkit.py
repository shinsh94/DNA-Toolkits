from structures import *
import collections

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq
    
def nucleotide_frequency(seq):
    """Count nucleotides in a given sequence. Return a dictionary"""
    tmpFreqDict = {"A":0, "C":0, "T":0, "G":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    #return dict(collections.Counter(seq))

def transcription(seq):
    """DNA -> RNA Transcription. Replacing T with U"""
    return seq.replace("T", "U")

def reverse_complement(seq):
    #return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::1]

def gc_content(seq):
    return round((seq.count('C')+seq.count('G'))/len(seq) * 100)

def gc_content_subsec(seq, k=10):
    res = []
    for i in range(0, len(seq)-k+1, k):
        subseq = seq[i:i+k]
        res.append(gc_content(subseq))
    return res