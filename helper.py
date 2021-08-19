def checkNGG(dictObject, index): 
    seqString = dictObject['seq']
    nLeftBound = int(index)
    if seqString[nLeftBound+1:nLeftBound+3] == 'gg':
        return True
    else:
        return False

def genCas9Parts(seqString, index, length5P, homologyPieceLeft5p, length3P, sgRNAlength): 
    nLeftBound = int(index) # use as end of grna substring
    if nLeftBound < sgRNAlength: 
        leftNucleotide = 0; 
    else: 
        leftNucleotide = nLeftBound - sgRNAlength
    gRNASubStr = seqString[leftNucleotide:nLeftBound]
    print(gRNASubStr)
    left5PHomologyArmSide = seqString[nLeftBound - homologyPieceLeft5p:nLeftBound]
    rightEnd = nLeftBound + 4 + length5P - homologyPieceLeft5p
    right5PHomologyArmSide = seqString[nLeftBound+4:rightEnd]
    full5PHomologyArm = left5PHomologyArmSide + 'caaa' + right5PHomologyArmSide
    print(full5PHomologyArm)
    full3PHomologyArm =  seqString[rightEnd:rightEnd+length3P]
    Cas9Parts = {}
    Cas9Parts['5PHomologyArm'] = full5PHomologyArm 
    Cas9Parts['3PHomologyArm'] = full3PHomologyArm
    Cas9Parts['sgRNA'] = gRNASubStr
    return Cas9Parts

def checkGCcontent(partDict): 
    gcContentLog = {}
    for part in partDict.keys(): 
        gcContentLog[part] = (part.count('g') + part.count('c')) / (len(part))
    return gcContentLog
