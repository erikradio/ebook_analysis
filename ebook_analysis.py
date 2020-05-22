import sys, re, uuid, csv
import pandas as pd

##this script counts field usage
with open(sys.argv[1], 'rU', errors='ignore') as csvFile:
    reader = csv.DictReader(csvFile)
    types = []
    fieldCount = {}
    for row in reader:
        type = row['Type']
        if type not in types:
            types.append(type)
    df = pd.read_csv(sys.argv[1])
    # df['Active_Cells'] = df.apply(lambda x: x.isnull().sum(), axis='columns')
    cols = df.columns.tolist()


    # print(df.isnull().sum())

    #this counts empty cells
    fieldCount=df.isnull().sum().to_dict()
    countRow=df.shape[0]
    print(countRow)
    for x in fieldCount:
        if fieldCount[x] > 0:
            fieldCount[x] =  countRow - fieldCount[x]
        else:
            fieldCount[x] = countro
    # print(fieldCount)

    # newCSV = pd.DataFrame(fieldCount).to_csv('out.csv', index=True)
    # (pd.DataFrame.from_dict(data=fieldCount, orient='columns')
    # .to_csv('file_name.csv', header=False))

    newdf = pd.DataFrame.from_records([fieldCount])
    (pd.DataFrame.from_dict(data=newdf, orient='columns')
    .to_csv('file_name.csv', header=True))
