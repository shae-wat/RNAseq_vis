# This program creates the final set of files to be fed into the gene drawing application.
# These files contain gene/ratio pairs, separated into files for each respective cluster.
# INPUT: set of files containing cluster data for a single species (output of geneSort.py),
# as well as a master file containing gene/expression data pairs for all genes in one species (output of splitRatios.py).
# OUTPUT: set of files containing gene/expression data pairs sorted into clusters.
# Each cluster file is compared to the master gene file; if a gene is present in both files, it is written
# (along with the expression data) to a new file corresponding to that cluster file.
# Essentially, this program pairs genes with their expression data, conserving cluster assortment.

def clusterFiles():
    print 'Processing...'

    # This file contains gene/ratio pairs for all genes in one species.
    # It can be created using the program splitRatios.py.
    geneFile = open("C:\\Python27\\Files\\Ratios\\newer_cer_hs_ratios.txt",'r+')

    # These files contain lists of genes corresponding to each cluster.
    # They can be created simultaneously using the program geneSort.py.
    hsClusters = open("C:\\Python27\\Files\\hscluster.txt",'r')
    oxClusters = open("C:\\Python27\\Files\\oxcluster.txt",'r')
    srClusters = open("C:\\Python27\\Files\\srcluster.txt",'r')
    tfClusters = open("C:\\Python27\\Files\\tfcluster.txt",'r')

    # These are the files that will be written to.
    hsFile = open("C:\\Python27\\Files\\Clusters\\Cerevisiae_heatShock.txt",'w')
    oxFile = open("C:\\Python27\\Files\\Clusters\\Cerevisiae_oxidativeResponse.txt",'w')
    srFile = open("C:\\Python27\\Files\\Clusters\\Cerevisiae_stressResponse.txt",'w')
    tfFile = open("C:\\Python27\\Files\\Clusters\\Cerevisiae_transcriptionFactor.txt",'w')
    noneFile = open("C:\\Python27\\Files\\Clusters\\Cerevisiae_noCluster.txt",'w')

    clusterDict = {}
    hsArray = []
    oxArray = []
    srArray = []
    tfArray = []


    # Put clusters into a dictionary for easy comparison to genes.
    for line in hsClusters:
        entry = line[0:-1]
        hsArray.append(entry)
    for line in oxClusters:
        entry = line[0:-1]
        oxArray.append(entry)
    for line in srClusters:
        entry = line[0:-1]
        srArray.append(entry)
    for line in tfClusters:
        entry = line[0:-1]
        tfArray.append(entry)


    # Puts cluster tags on each gene in the dictionary and counts them. Also creates a new dictionary,
    # containing genes matched with their expression ratios ([gene:ratio]). 
    hsCount = 0
    oxCount = 0
    srCount = 0
    tfCount = 0
    noneCount = 0
    ratioDict = {}

    ########
    # NOTE #
    ########
    # This next loop splits each line of the gene file into genes and ratios. The code is written
    # specifically for the files created by splitRatios.py, formatted with two tab delimiters
    # separating the genes and ratios. Be sure your files match this format (if you created them with
    # splitRatios.py, you will encounter no problems).
    for line in geneFile:
        gene = line.split('\t\t')[0]
        ratio = line.split('\t\t')[1]
        # This segment removes newlines from the end of the ratio string
        ratioList = []
        for ch in ratio:
            if ord(ch) != 10:
                ratioList.append(ch)
            newRatio = ''
            for r in ratioList:
                newRatio += r
                ratioDict[gene] = newRatio
        # and adds them to the dictionary.
        clusterDict[gene] = []

        # This loop adds 'cluster tags' to the entries of the dictionary.
        # These serve to essentially 'tag' each gene with its corresponding cluster.
        for hs in hsArray:
            if gene == hs:
                clusterDict[gene].append('hs')
                hsCount += 1
        for ox in oxArray:
            if gene == ox:
                clusterDict[gene].append('ox')
                oxCount += 1
        for sr in srArray:
            if gene == sr:
                clusterDict[gene].append('sr')
                srCount += 1
        for tf in tfArray:
            if gene == tf:
                clusterDict[gene].append('tf')
                tfCount += 1

    for gene in clusterDict:
        if clusterDict[gene] == []:
            clusterDict[gene].append('none')
            noneCount += 1

                                         
    # Writes counters to respective files
    hsCountStr = 'Gene Count: ' + str(hsCount) + '\n\n'
    hsFile.write(hsCountStr)
    oxCountStr = 'Gene Count: ' + str(oxCount) + '\n\n'
    oxFile.write(oxCountStr)
    srCountStr = 'Gene Count: ' + str(srCount) + '\n\n'
    srFile.write(srCountStr)
    tfCountStr = 'Gene Count: ' + str(tfCount) + '\n\n'
    tfFile.write(tfCountStr)
    noneCountStr = 'Gene Count: ' + str(noneCount) + '\n\n'
    noneFile.write(noneCountStr)


    # Writes gene/ratio pairs to cluster files.
    for gene in clusterDict:
        ratio = ratioDict[gene]
        geneStr = gene + '\t' + ratio + '\n'
        for i in range(len(clusterDict[gene])):
            if clusterDict[gene][i] == 'hs':
                hsFile.write(geneStr)
            elif clusterDict[gene][i] == 'ox':
                oxFile.write(geneStr)
            elif clusterDict[gene][i] == 'sr':
                srFile.write(geneStr)
            elif clusterDict[gene][i] == 'tf':
                tfFile.write(geneStr)
            else:
                noneFile.write(geneStr)

    geneFile.close()
    hsClusters.close()
    oxClusters.close()
    srClusters.close()
    tfClusters.close()

    hsFile.close()
    oxFile.close()
    srFile.close()
    tfFile.close()
    noneFile.close()
    
    print 'Done!'


#if __name__ == '__main__':
#    clusterFiles()
