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