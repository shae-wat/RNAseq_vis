# This program sorts genes by their cluster tags into respective files.
# INPUT: file of genes from one species, each with corresponding cluster tag(s).
# OUTPUT: set of files, each corresponding to a specific cluster.
#####
# The files printed from this program are for use in the program clusterFiles.py.
# They are used in conjunction with the output from the program splitRatios.py.

def geneSort():
    print 'Processing...'
    # Opens files being read or written to
    inFile = open('E:\\newClusters.txt', 'r+')
    hsClusterFile = open('C:\\Python27\\Files\\hscluster.txt', 'w')
    oxClusterFile = open('C:\\Python27\\Files\\oxcluster.txt', 'w')
    srClusterFile = open('C:\\Python27\\Files\\srcluster.txt', 'w')
    tfClusterFile = open('C:\\Python27\\Files\\tfcluster.txt', 'w')
    hscounter = 0
    oxcounter = 0
    srcounter = 0
    tfcounter = 0

                
    # Splits each line of the main cluster file into genes and their cluster tags.
    # Then sorts each gene to any of the files matching its tag.
    # Also counts the number of genes in each cluster.
    for line in inFile:
        gene = line.split('\t')[0]
        response = line.split('\t')[1]
        responseCharList = list(response)
        for i in range(len(responseCharList) - 1):
            tempCharList = ''
            tempCharList = tempCharList + responseCharList[i] + responseCharList[i+1]
            if tempCharList == 'hs':
                hsClusterFile.write(gene)
                hsClusterFile.write('\n')
                hscounter += 1
            elif tempCharList == 'ox':
                oxClusterFile.write(gene)
                oxClusterFile.write('\n')
                oxcounter += 1
            elif tempCharList == 'sr':
                srClusterFile.write(gene)
                srClusterFile.write('\n')
                srcounter += 1
            elif tempCharList == 'tf':
                tfClusterFile.write(gene)
                tfClusterFile.write('\n')
                tfcounter += 1

    # Writes the number of genes in each cluster to respective file.            
    hsHeader = 'There are ' + str(hscounter) + ' genes in this file.'
    hsClusterFile.seek(0)
    hsClusterFile.write(hsHeader)
    hsClusterFile.write('\n')
    hsClusterFile.write('\n')

    oxHeader = 'There are ' + str(oxcounter) + ' genes in this file.'
    oxClusterFile.seek(0)
    oxClusterFile.write(oxHeader)
    oxClusterFile.write('\n')
    oxClusterFile.write('\n')

    srHeader = 'There are ' + str(srcounter) + ' genes in this file.'
    srClusterFile.seek(0)
    srClusterFile.write(srHeader)
    srClusterFile.write('\n')
    srClusterFile.write('\n')

    tfHeader = 'There are ' + str(tfcounter) + ' genes in this file.'
    tfClusterFile.seek(0)
    tfClusterFile.write(tfHeader)
    tfClusterFile.write('\n')
    tfClusterFile.write('\n')

    
    inFile.close()
    hsClusterFile.close()
    oxClusterFile.close()
    srClusterFile.close()
    tfClusterFile.close()
    print 'Done!'

#if __name__ == '__main__':
#    geneSort()
