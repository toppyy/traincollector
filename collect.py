import requests
import datetime
import time
import os
import sys


arguments = sys.argv


collectionDelay = 5

if len(arguments)>1:
    collectionDelay = int(arguments[1])
    

url = 'https://rata.digitraffic.fi/api/v1/train-locations/latest/'


datapath = './data/'

if os.path.exists(datapath) == False:
    os.mkdir(datapath)

filename = './data/data.csv'

if os.path.exists(filename):
    append_write = 'a' 
else:
    append_write = 'w' 


datafile = open(filename,append_write)


def dictToCSV(d,delimiter=";"):

    res = []

    for k in d.keys():
        if k=='location':
            coords = d[k]["coordinates"]
            res.append(coords[0])
            res.append(coords[1])
        else:
            res.append(d[k])

    return delimiter.join(list(map(str,res)))



while True:

    
    r = requests.get(url)
    data = r.json()

    asCSV = list(map(dictToCSV,data))

    datafile.writelines('\n'.join(asCSV))
    datafile.write('\n')

    print('Collected train locations. Delaying next collection for {} seconds'.format(collectionDelay))
    time.sleep(collectionDelay)