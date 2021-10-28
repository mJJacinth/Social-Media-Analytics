import pandas as pd
def makeDataFrame(filename):
    str=pd.read_csv(filename)
    # print(str)
    return str
print(makeDataFrame("data/politicaldata.csv"))