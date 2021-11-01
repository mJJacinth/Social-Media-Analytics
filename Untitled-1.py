import pandas as pd
import csv
# def makeDataFrame(filename):
#     str=pd.read_csv(filename)
#     # print(str)
#     return str
# print(makeDataFrame("data/politicaldata.csv"))

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



def findHashtags(message):
    temp1=[]
    temp= message.split(" ")
    for i in temp:
        if i[0] == "#":
            temp1.append(i)
    for i in temp1:
        if endChars
    # return
findHashtags("I am so #excited to watch #TheMandalorian! #starwars") == [ "#excited", "#TheMandalorian", "#starwars" ]