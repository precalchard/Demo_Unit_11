import pandas
import matplotlib as plot

data = pandas.read_csv("zooData.csv")

plot.figure(figsize=(8,8))

plot.plot(kind="bar", x=data["Animal"], y=data["Count"])

