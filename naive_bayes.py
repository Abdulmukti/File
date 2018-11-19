import csv
import numpy as np
import operator
with open('insurance.csv') as data:
    reader = csv.reader(data)
    attribut = next(reader)
    attName = [attribut[i] for i in range(len(attribut)-1)]
    data = []
    for row in reader:
        data.append(row)
cI = len(data[0])-1

cG = []
for cd in data:
    if cd[cI] not in cG:
        cG.append(cd[cI])

dS = {}
dM = {}
for cN in cG:
    tempDataMean = {}
    tempDataStd = {}
    for i in range(len(data[0])-1):
        attname = attName[i]
        tempColData = []
        for j in range(len(data)):
            if data[j][cI] == cN:
                tempColData.append(float(data[j][i]))
        countMean = np.mean(tempColData)
        tempDataMean[attname] = countMean
        countStd = np.std(tempColData,ddof=1)
        tempDataStd[attname] = countStd
    dM[cN] = tempDataMean
    dS[cN] = tempDataStd


oppClass = {}
for cN in cG:
    countClass = 0
    for i in range(len(data)):
        if data[i][cI] == cN:
            countClass += 1
    oppClass[cN] = countClass/len(data)
    
def opportunity(attname, value, cN):
    countOp = (1/((2*np.pi)**0.5)*dS[cN][attname])* \
              ((np.exp(1)**(-(((value-dM[cN][attname])**2)/ \
                              (2*((dS[cN][attname])**2))))))
    return countOp

def test(row):
    oDTest = {}
    oDTest.update(oppClass)
    for i in range(len(attName)):
        value = float(row[i])
        for cN in cG:
            oDTest[cN] *= opportunity(attName[i], value, cN)
    return (max(oDTest.items(), key=operator.itemgetter(1))[0])


def data():
    oD = {}
    oD.update(oppClass)
    for attname in attName:
        value = float(input('Masukkan value %s = '%attname))
        for cN in cG:
            oD[cN] *= opportunity(attname, value, cN)
           
    return (max(oD.items(), key=operator.itemgetter(1))[0])

print(data())
