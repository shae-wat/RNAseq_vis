# This program takes a file of genes matched with expression data for the four research strains of
# Saccharomyces and splits it into separate files for each species.
# INPUT: a file containing expression data for all genes shared by the four subject Saccharomyces
# species (Cerevisiae, Bayanus, Mikatae, and Paradoxus).
# OUTPUT: set of four files, each containing cluster data for a single species.
#####
# The files printed from this program are for use in the program clusterFiles.py.
# They are used in conjunction with the output from the program geneSort.py.


import string

def splitRatios():
    bayDict = {}
    cerDict = {}
    mikDict = {}
    parDict = {}
    bayGeneCount = 0
    cerGeneCount = 0
    mikGeneCount = 0
    parGeneCount = 0
    print 'Writing...'
    # Opens files to be read/written to
    inFile = open("C:\\Users\\Nick\\Desktop\\ratios.txt",'r')
    bayFile = open("C:\\Python27\\Files\\Ratios\\new_bay_hs_ratios.txt",'w')
    cerFile = open("C:\\Python27\\Files\\Ratios\\new_cer_hs_ratios.txt",'w')
    mikFile = open("C:\\Python27\\Files\\Ratios\\new_mik_hs_ratios.txt",'w')
    parFile = open("C:\\Python27\\Files\\Ratios\\new_par_hs_ratios.txt",'w')
    
    # Reads entire file into a string, then splits it into individual ratios.
    ########
    # NOTE #
    ########
    # This next part of the code is written specifically for the file we had created before writing this
    # splitting program. Therefore, it follows the specific formatting of the file; each line consists of
    # a gene ID followed by four expression ratios (one for each species), with all ratios separated by one
    # tab delimiter.
    #            Ex: YAL065C   1.664970    1.358043    #   0.655454
    # Ensure your input file matches these formatting specifics. The # symbol indicates no read for that species.
    fileStr = inFile.read()
    geneList = fileStr.split('\n')
    for i in range(len(geneList)-1):
        ratios = geneList[i].split('\t')
        geneName = ratios[0]
        if ratios[1] != '#':
            bayGeneCount += 1
            bayDict[geneName] = ratios[1]
        if ratios[2] != '#':
            cerGeneCount += 1
            cerDict[geneName] = ratios[2]
        if ratios[3] != '#':
            mikGeneCount += 1
            mikDict[geneName] = ratios[3]
        if ratios[4] != '#':
            parGeneCount += 1
            parDict[geneName] = ratios[4]

    bayCountStr = 'Gene count: ' + str(bayGeneCount) + '\n\n'
    cerCountStr = 'Gene count: ' + str(cerGeneCount) + '\n\n'
    mikCountStr = 'Gene count: ' + str(mikGeneCount) + '\n\n'
    parCountStr = 'Gene count: ' + str(parGeneCount) + '\n\n'

    bayFile.write(bayCountStr)
    cerFile.write(cerCountStr)
    mikFile.write(mikCountStr)
    parFile.write(parCountStr)

    ########
    # NOTE #
    ########
    # This last snippet writes the gene/expression ratio pairs to their corresponding files.
    # The output files of this program are used as input in the follow up program clusterFiles.py.
    # If you are planning on using this program to split your data into clusters, be sure your formatting is correct.
    for key,value in bayDict.items():
        printStr = key + '\t\t' + value + '\n'
        bayFile.write(printStr)
    for key,value in cerDict.items():
        printStr = key + '\t\t' + value + '\n'
        cerFile.write(printStr)
    for key,value in mikDict.items():
        printStr = key + '\t\t' + value + '\n'
        mikFile.write(printStr)
    for key,value in parDict.items():
        printStr = key + '\t\t' + value + '\n'
        parFile.write(printStr)

    inFile.close()
    bayFile.close()
    cerFile.close()
    mikFile.close()
    parFile.close()
    print 'Done!'


#if __name__ == '__main__':
#    splitRatios()

