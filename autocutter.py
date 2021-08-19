import click
from click.termui import prompt
from helper import checkGCcontent, checkNGG, genCas9Parts
from snapgene_reader import snapgene_file_to_dict, snapgene_file_to_seqrecord
import json

@click.command()
@click.option('--dfile', prompt='.dna file', help='file to use')
@click.option('--insertionpoint', prompt='cas9 cutsite', help='where to cut')
@click.option('--seqfile', default='seq.txt',help='filename to dump sequences in')
@click.option('--gccontentfile',default='gccontent.txt',help='filename to gccontent in')
@click.option('--homologylength5p', default=550,help='total length of 5 prime homology, 500-600 bp optimal')
@click.option('--homologypieceleft5p', default=500,help='left part of the 5 prime')
@click.option('--homologylength3p', default=550, help='total length of 3 prime homology,  500-600 bp optimal')
@click.option('--sgrnalength', default=15, help='length of sgrna, 5-25 bp optimal')

def execute(dfile, insertionpoint, seqfile, gccontentfile, homologylength5p, homologypieceleft5p, homologylength3p, sgrnalength):
    fileName = dfile; 
    print(fileName)
    print('before parse')
    dictObject = snapgene_file_to_dict(fileName)
    seqOutputFile = seqfile 
    gcContentOutputFile = gccontentfile
    length5P = int(homologylength5p)
    length3P = int(homologylength3p)
    homologyPieceLeft5p = homologypieceleft5p
    sgRNAlength = sgrnalength
    if not bool(dictObject): 
        print ("not parsable")
        return 0 
    ssSeq = dictObject['seq']
    if checkNGG(dictObject, insertionpoint):
        print("can cut")
        cas9Dict = genCas9Parts(ssSeq, insertionpoint, int(length5P), int(homologyPieceLeft5p), int(length3P), int(sgRNAlength))
    gcContent = checkGCcontent(cas9Dict)
    with open(seqOutputFile, 'w') as seq_output:
        seq_output.write(json.dumps(cas9Dict))
    with open(gcContentOutputFile, 'w') as gc_output:
        gc_output.write(json.dumps(gcContent))
    

if __name__ == "__main__":
    execute()
