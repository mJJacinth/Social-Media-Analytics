"""
Social Media Analytics Project
Name:
Roll Number:
"""

from typing import Counter
from nltk.tag import pos_tag
import hw6_social_tests as test
from collections import Counter

project = "Social" # don't edit this

### PART 1 ###

import pandas as pd
import nltk
nltk.download('vader_lexicon', quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
endChars = [ " ", "\n", "#", ".", ",", "?", "!", ":", ";", ")" ]
#  str=pd.DataFrame(politicaldata.csv)

'''
makeDataFrame(filename)
#3 [Check6-1]
Parameters: str
Returns: dataframe
'''
def makeDataFrame(filename):
    str=pd.read_csv(filename)
    return str


'''
parseName(fromString)
#4 [Check6-1]
Parameters: str
Returns: str
'''
def parseName(fromString):
    temp=fromString.split(":")[1]
    temp=temp.split("(")[0]
    temp=temp.split(" ")
    if len(temp)>3:
        name=str(temp[1])+" "+str(temp[2])
    else:
        name=str(temp[1])
    return name
    


# print(parseName("data/politicaldata.csv"))


'''
parsePosition(fromString)
#4 [Check6-1]
Parameters: str
Returns: str
'''
def parsePosition(fromString):
    temp=fromString.split("(")[1]
    temp=temp.split(")")[0]
    temp=temp.split(" ")
    name=""
    if len(temp)==3:
        name=str(temp[0])
    return name
    
# parsePosition("From: Steny Hoyer (Representative from Maryland)")



'''
parseState(fromString)
#4 [Check6-1]
Parameters: str
Returns: str
'''
def parseState(fromString):
    temp=fromString.split("(")[1]
    temp=temp.split(")")[0]
    temp=temp.split(" ")
    if len(temp)==3:
        name=str(temp[2])
    else:
        name= str(temp[2])+" "+str(temp[3])
    return name


'''
findHashtags(message)
#5 [Check6-1]
Parameters: str
Returns: list of strs
'''
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


''' 
getRegionFromState(stateDf, state)
#6 [Check6-1]
Parameters: dataframe ; str
Returns: str
'''
def getRegionFromState(stateDf, state):
    row=stateDf.loc[stateDf["state"] == state, "region"]
    return row.values[0]


'''
addColumns(data, stateDf)
#7 [Check6-1]
Parameters: dataframe ; dataframe
Returns: None
'''
def addColumns(data, stateDf):
    names=[]
    positions=[]
    states=[]
    regions=[]
    hashtags=[]
    for index, row in data.iterrows():
        val=row["label"]
        # val1=row["text"]
        names.append(parseName(val))
        positions.append(parsePosition(val))
        state=parseState(val)
        states.append(parseState(val))
        regions.append(getRegionFromState(stateDf,state))
        hashtags.append(findHashtags(data["text"][index]))        
    data['name']=names
    data['position']=positions
    data['state']=states
    data['region']=regions
    data['hashtags']=hashtags
    return


### PART 2 ###

'''
findSentiment(classifier, message)
#1 [Check6-2]
Parameters: SentimentIntensityAnalyzer ; str
Returns: str
'''
def findSentiment(classifier, message):
    score = classifier.polarity_scores(message)['compound']
    if score > 0.1:
        return  "positive"
    if score < -0.1:
        return "negative"
    else:
        return "neutral"
'''
addSentimentColumn(data)
#2 [Check6-2]
Parameters: dataframe
Returns: None
'''
def addSentimentColumn(data):
    classifier = SentimentIntensityAnalyzer()
    sentiments=[]
    for index, row in data.iterrows():
        message=row["text"]
        var=findSentiment(classifier,message)
        sentiments.append(var)

    data["sentiment"]=sentiments
    return 


'''
getDataCountByState(data, colName, dataToCount)
#3 [Check6-2]
Parameters: dataframe ; str ; str
Returns: dict mapping strs to ints
'''
def getDataCountByState(data, colName, dataToCount):
    dict={}
    for index,row in data.iterrows():
        if colName=="" and dataToCount=="":
            if row["state"] not in dict:
                dict[row["state"]]=0
            dict[row["state"]]+=1
        elif row[colName]==dataToCount:
            if row["state"] not in dict:
                dict[row["state"]]=0
            dict[row["state"]]+=1
    return dict


'''
getDataForRegion(data, colName)
#4 [Check6-2]
Parameters: dataframe ; str
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def getDataForRegion(data, colName):
    dict={}
    for index,row in data.iterrows():
        if row["region"] not in dict:
            dict[row["region"]]={}
        if row[colName] not in dict[row["region"]]:
            dict[row["region"]][row[colName]]=0
        dict[row["region"]][row[colName]]+=1 
    return dict


'''
getHashtagRates(data)
#5 [Check6-2]
Parameters: dataframe
Returns: dict mapping strs to ints
'''
def getHashtagRates(data):
    dict={}
    for row in data["hashtags"]:
        for i in row:
            if i not in dict and len(i)!=0:
                dict[i]=1
            else:
                dict[i]=dict[i]+1
    return dict
    # print(dict)



        


'''
mostCommonHashtags(hashtags, count)
#6 [Check6-2]
Parameters: dict mapping strs to ints ; int
Returns: dict mapping strs to ints
'''
def mostCommonHashtags(hashtags, count):
    dict={}
    while len(dict)!=count:
        large=0
        for each in hashtags:
            print(each)
            if each not in dict and hashtags[each]>large:
                large=hashtags[each]
                key=each
        dict[key]=large
    return dict


'''
getHashtagSentiment(data, hashtag)
#7 [Check6-2]
Parameters: dataframe ; str
Returns: float
'''
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
    return num/count


### PART 3 ###

'''
graphStateCounts(stateCounts, title)
#2 [Hw6]
Parameters: dict mapping strs to ints ; str
Returns: None
'''
def graphStateCounts(stateCounts, title):
    import matplotlib.pyplot as plt
    key=[]
    val=[]
    for i,j in stateCounts.items():
        key.append(i)
        val.append(j)
    for index in range(len (val)): 
        plt.bar(key[index],val[index])
    plt.xticks(ticks=list(range(len(val))),labels=key,rotation="vertical")
    plt.title(title)
    plt.show()
    return


'''
graphTopNStates(stateCounts, stateFeatureCounts, n, title)
#3 [Hw6]
Parameters: dict mapping strs to ints ; dict mapping strs to ints ; int ; str
Returns: None
'''
def graphTopNStates(stateCounts, stateFeatureCounts, n, title):
    rate={}
    states={}
    for i in stateFeatureCounts:
        rate[i]=(stateFeatureCounts[i]/stateCounts[i])
    states=dict(Counter(rate).most_common(n))
    graphStateCounts(states,title)
    return


'''
graphRegionComparison(regionDicts, title)
#4 [Hw6]
Parameters: dict mapping strs to (dicts mapping strs to ints) ; str
Returns: None
'''
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


'''
graphHashtagSentimentByFrequency(data)
#4 [Hw6]
Parameters: dataframe
Returns: None
'''
def graphHashtagSentimentByFrequency(data):
   
    return


#### PART 3 PROVIDED CODE ####
"""
Expects 3 lists - one of x labels, one of data labels, and one of data values - and a title.
You can use it to graph any number of datasets side-by-side to compare and contrast.
"""
def sideBySideBarPlots(xLabels, labelList, valueLists, title):
    import matplotlib.pyplot as plt

    w = 0.8 / len(labelList)  # the width of the bars
    xPositions = []
    for dataset in range(len(labelList)):
        xValues = []
        for i in range(len(xLabels)):
            xValues.append(i - 0.4 + w * (dataset + 0.5))
        xPositions.append(xValues)

    for index in range(len(valueLists)):
        plt.bar(xPositions[index], valueLists[index], width=w, label=labelList[index])

    plt.xticks(ticks=list(range(len(xLabels))), labels=xLabels, rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Expects that the y axis will be from -1 to 1. If you want a different y axis, change plt.ylim
"""
def scatterPlot(xValues, yValues, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xValues, yValues)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xValues[i], yValues[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.ylim(-1, 1)

    # a bit of advanced code to draw a line on y=0
    ax.plot([0, 1], [0.5, 0.5], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    test.week1Tests()
    print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    test.runWeek1()


    ## Uncomment these for Week 2 ##
    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    test.runWeek2()
    

    ## Uncomment these for Week 3 ##
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()
