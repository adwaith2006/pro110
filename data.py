import random
import statistics as st
import csv
import pandas as pd
import plotly.figure_factory as ff 

df=pd.read_csv("medium_data.csv")
data=df["claps"].to_list()
population_mean=st.mean(data)
print("mean of population data is:",population_mean)

def randomSetOfMean(counter):
    data_set=[]
    for i in range(0,counter):

        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)

    population_mean=st.mean(data_set)
    return(population_mean)

def showFig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["claps"],show_hist=False)
    fig.show()
    sample_mean=st.mean(mean_list)
    print("mean of sample data is:",sample_mean)
    
def setUp():
    mean_list=[]
    for i in range(0,100):
        setOfMean=randomSetOfMean(30)
        mean_list.append(setOfMean)

    showFig(mean_list)

setUp()


