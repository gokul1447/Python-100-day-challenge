import pandas as pd

data=pd.read_csv("Squiral/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250407.csv")
gray=(len(data[data["Primary Fur Color"]=="Gray"]))
red=(len(data[data["Primary Fur Color"]=="Cinnamon"]))
black=(len(data[data["Primary Fur Color"]=="Black"]))

dict={
    "color":["gray","red","black"],
    "count": [ gray,red,black]
}

df=pd.DataFrame(dict)
print(df)

#df.to_csv("squiral.csv")