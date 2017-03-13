# clusters.py from Collective Intelligence by Toby Segaran
# potentially edited by J. Macoskey

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
        data.append([float(x) for x in p[1:])
    return (rownames,colnames,data)
    
def pearson(v1,v2):
    sum1 = sum(v1)
    sum2 = sum(v2)

    sum1sq = sum([pow(v,2) for v in v1])
    sum2sq = sum([pow(v,2) for v in v2])

    sumProd = sum([v1[i]*v2[i] for i in range(len(v1))])

    num = sumProd - (sum1*sum2/len(v1))
    den = sqrt((sum1sq-pow(sum1,2)/len(v1))*(sum2sq-pow(sum2,2)/len(v1)))
    if den == 0:
        return 0
    return 1.0-num/den


