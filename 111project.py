import pandas as pd
import csv
import statistics
import random

df = pd.read_csv("111projectdata.csv")
data = df["readingtime"].tolist()
mean = statistics.mean(data)
print(mean)

stdev = statistics.stdev(data)
print(stdev)

def random_set_of_data(counter):
    datasheet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        datasheet.append(value)
    mean1 = statistics.mean(datasheet)
    return mean1    

def setUp():
    mean_list = []
    for i in range(0,100):
        set_of_mean = random_set_of_data(30)
        mean_list.append(set_of_mean)
    mean1 = statistics.mean(mean_list)
    return mean1
    print("sampling mean is:-",mean1) 

setUp()

zscore = (mean-mean1)/stdev
print(zscore)


