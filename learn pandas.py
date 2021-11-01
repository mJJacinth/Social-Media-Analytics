import pandas as pd
d={"name": [ "Jem", "Blessy", "Jacinth","Nissi" ],
   "year": [ "junior", "junior", "senior","senior"],
   "major":["psychology","cs","ece","mbbs"]
   }
df=pd.DataFrame(d)
print(df)
print(df["name"])
print(df["year"])
print(df["major"])
df["Ice-cream"]= ["butterscotch","choco delight","brownie","litchie"]
print(df)
for index, row in df.iterrows():
    print(index)
    print(row)
    print("Name:" ,row["name"])
    print()