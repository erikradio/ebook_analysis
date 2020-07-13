import sys, re, uuid, csv
from scipy import stats
import pandas as pd

#use bibs_201910_ebookvid_webpacdata_4_10_2020.csv

with open(sys.argv[1], 'rU', errors='ignore') as csvFile, open(sys.argv[2],'w') as csvOut:
    # reader = csv.DictReader(csvFile)


    #THIS COUNTS 856z DATA in MARC
    # newdict = {}
    df = pd.read_csv(csvFile)

#THIS WORKS FOR MARC DATA
    # df['6500'] = df['6500'].dropna().astype(str)
    # subj=df['6500'].str.count('\|') + 1
    # df['subjectCount'] = subj
    #
    #
    #
    # df['6510'] = df['6510'].dropna().astype(str)
    # geo=df['6500'].str.count('\|') + 1
    # df['geoCount'] = geo
    # # #
    #
    # df['653a'] = df['653a'].dropna().astype(str)
    # indexCount=df['653a'].str.count('\|') + 1
    # df['indexTermCount'] = indexCount
    # # #
    # df['690a'] = df['690a'].dropna().astype(str)
    # local1=df['690a'].str.count('\|') + 1
    # df['localField1Count'] = local1
    # #
    #
    # df['690x'] = df['690x'].dropna().astype(str)
    # local2=df['690x'].str.count('\|') + 1
    # df['local2Count'] = local2
    # #
    #
    # df['6550'] = df['6550'].dropna().astype(str)
    # genreCount=df['6550'].str.count('\|') + 1
    # df['genreCount'] = genreCount

    # THIS WORKS FOR WEBPAC Data
    newdf = pd.DataFrame(columns = ['subjectCount', 'clicks'])
    df['Subject'] = df['Subject'].dropna().astype(str)
    subj=df['Subject'].str.count('\|') + 1
    newdf['subjectCount'] = subj.fillna(0).astype(int)
    # print(df['subjectCount'])

    # newdf['subjectCount'] = df['subjectCount'].fillna('0')
    newdf['clicks'] = df['clicks'].fillna(0).astype(int)

    # newdf = newdf.dropna()
    print(stats.spearmanr(newdf['subjectCount'], newdf['clicks']))

    # #
    # print(newdf.corr('spearman'))
