# cas9partsmaker
Simple command line tool to generate sequences needed for crispr cas9 genome edits. 

## Dependencies 
Need to install Snapgene Reader and Click command line. 

`pip install snapgene_reader` 

`pip install click` 

## Basic Usage
`python autocutter.py --dfile=[your .dna file here] --insertionpoint=[place you want to make the cut]`

or `python autocutter.py` , you will be prompted for the .dna file and insertion point. 

## Instructions 
1. Find the host/native genome of your organism online, import the .dna file into SnapGene or which ever plasmid viewer application you see fit. Most applications allow imports if you have the accession number, which is usually given on the NCBI website. 
2. Assuming you are using spCas9 protein, find the location where you want to cut. That is to the left of the N in the NGG (PAM sequence for spCas9). This is the insertion point number. 
3. Enter those parameters into the initial command line call OR just let it prompt you. 
4. Additional options allow customization of the output filenames (text file that contains sequences), length of homology regions (500-600 bp is recommended), and length of sgRNA sequence. 

`--seqfile=[your file name here]`

`--gccontentfile=[your file name here]`

`--homologylength5p=[total length of 5 prime homology length]`

`--homologypieceleft5p=[length of the 5 prime homology piece to the left of the cut]`

`--homologylength3p=[total length of 3 prime homology length]`

`--sgrnalength=[total length of 3sgrna]`
