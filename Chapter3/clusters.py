# clusters.py from Collective Intelligence by Toby Segaran
# partially edited by J. Macoskey - 2017

from math import sqrt

def readfile(filename):
    lines = [line for line in file(filename)]

    # first line is the column titles
    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []
    for line in lines[1:]:
        p = line.strip().split('\t')
        # first column in each row is the rowname
        rownames.append(p[0])
        # the data for this row is the remainder of the row
        data.append([float(x) for x in p[1:]])
    return (rownames,colnames,data)
    
def pearson(v1,v2):
    sum1 = sum(v1)
    sum2 = sum(v2)

    sum1sq = sum([pow(v,2) for v in v1])
    sum2sq = sum([pow(v,2) for v in v2])

    # some may have different lengths - take the minimum
    sumProd = sum([v1[i] * v2[i] for i in min(range(len(v1)),range(len(v2)))])

    # tell me if they had different lengths
    if range(len(v1)) != range(len(v2)):
        print "mismatched length"

    num = sumProd - (sum1*sum2/len(v1))
    den = sqrt((sum1sq-pow(sum1,2)/len(v1))*(sum2sq-pow(sum2,2)/len(v1)))
    if den == 0:
        return 0
    return 1.0-num/den

class bicluster:
    def __init__(self,
                 vec,
                 left=None,
                 right=None,
                 distance=0.0,
                 id=None):
                 self.left=left
                 self.right=right
                 self.vec=vec
                 self.id=id
                 self.distance=distance

def hcluster(rows,distance=pearson):
    distances = {}
    currentclustid = -1

    clust = [bicluster(rows[i],id=i) for i in range(len(rows))]

    while len(clust) > 1:
        lowestpair = (0,1)
        closest = distance(clust[0].vec,clust[1].vec)

        # loop through every pari looking for the smallest distance
        count = 1
        for i in range(len(clust)):
            for j in range(i+1,len(clust)):
            # distances is the cache of distance calcuations. 
            # This is like the Pij matrix.
                try:
                    if (clust[i].id,clust[j].id) not in distances:
                        distances[(clust[i].id,clust[j].id)]= \
                            distance(clust[i].vec,clust[j].vec)
                    # print "%d of %d" % (count,i*j)
                    # count += 1

                    d = distances[(clust[i].id,clust[j].id)]

                    if d < closest:
                        closest = d
                        lowestpair = (i,j)
                except:
                    # print "failed something"
                    count += 1
        print "%d of %d failed" % (count, i*j)

# calculate the average of the two clusters
        mergevec = [(clust[lowestpair[0]].vec[i]+clust[lowestpair[1]].vec[i])/2
        for i in range(len(clust[0].vec))]

# create the new cluster
        newcluster=bicluster(mergevec,left=clust[lowestpair[0]],
        right=clust[lowestpair[1]],distance = closest, id = currentclustid)

# cluster ids that weren't in the original set are negative
        currentclustid = -1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(newcluster)
    return clust[0]

def printclust(clust,labels=None,n=0):
    # indent to make heirarchy layout
    for i in range(n): print ' ',
    if clust.id < 0:
        # negative id meansthat this is branch
        print '-'
    else:
        # positive id means that this is an endpoint
        if labels == None: print clust.id
        else: print labels[clust.id]

    # now print the right and left branches
    if clust.left != None: printclust(clust.left,labels=labels,n=n+1)
    if clust.right != None: printclust(clust.right,labels=labels,n=n+1)



