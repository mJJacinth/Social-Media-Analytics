import pandas as pd
import csv
def makeDataFrame(filename):
    str=pd.read_csv(filename)
    # print(str)
#     return str
makeDataFrame("data/politicaldata.csv")

# def parseName(fromString):
#     f = open('data/politicaldata.csv')
#     temp=fromString.split(":")[1]
#     temp=temp.split("(")[0]
#     print(temp)
# parseName("From: Steny Hoyer (Representative from Maryland)")

# def parsePosition(fromString):
#     temp=fromString.split("(")[1]
#     temp=temp.split(")")[0]
#     temp=temp.split(" ")
#     if len(temp)==3:
#         name=temp
#     print(temp)
    
# parsePosition("From: Steny Hoyer (Representative from Maryland)")
endChars = [ " ", "\n", "#", ".", ",", "?", "!", ":", ";", ")" ] 

def findHashtags(message):
    res=[]
    temp= message.split("#")
    for i in temp[1:]:
        temp1="#"
        for j in i:
            if j in endChars:
                break
            temp1=temp1+j
        res.append(temp1)
    return res

data="data/politicaldata.csv"
hashtag="#jobs"
def getHashtagSentiment(data, hashtag):
    num=0
    count=0
    for index,row in data.iterrows():
        hashtags=findHashtags(row["text"])
        if hashtag in hashtags:
            count=count+1
            if row["sentiment"]=="positive":
                num=num+1        
            elif row["sentiment"]=="negative":
                num=num-1
            elif row["sentiment"]=="neutral":
                num=num+0
    print(num/count)
getHashtagSentiment(data, hashtag)


def graphTopNStates(stateCounts, stateFeatureCounts, n, title):
    rate={}
    states={}
    for i in stateFeatureCounts:
        rate[i]=(stateFeatureCounts[i]/stateCounts[i])
    states=dict(Counter(rate).most_common(n))
    graphStateCounts(states,title)
    return

def graphRegionComparison(regionDicts, title):
    list=[]
    region=[]
    value=[]
    for i in regionDicts:
        temp=[]
        for j in regionDicts[i]:
            if j not in list:
                list.append(j)
            temp.append(regionDicts[i][j])
        value.append(list)
        region.append(i)
    sideBySideBarPlots(list,region,value,title)
    return
def graphHashtagSentimentByFrequency(data):
    lst=[]
    freq=[]
    score=[]
    rates=getHashtagRates(data)
    tags=mostCommonHashtags(rates,50)
    for i,j in tags.items():
        lst.append(i)
        freq.append(j)
        sentiment=getHashtagSentiment(data,i)
        score.append(sentiment)    
    scatterPlot(freq,score,lst,"SentimentByFrequency")
    return