import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

df = pd.read_csv("sample_1.csv")
time = df["reading_time"].tolist()
mean_of_sample_1 = statistics.mean(time)

figure = ff.create_distplot([mean_list], ["Mean Graph"],show_hist=False)
figure.add_trace(go.Scatter(x = [mean,mean], y = [0,1.4], mode = "lines", name = "mean"))
figure.add_trace(go.Scatter(x = [mean_of_sample_1,mean_of_sample_1],y = [0,1.4],mode = "lines",name = "Mean of students who were given math tabs"))
figure.show()

df = pd.read_csv("sample_2.csv")
time = df["reading_time"].tolist()
mean_of_sample_2 = statistics.mean(time)

figure = ff.create_distplot([mean_list], ["Mean Graph"],show_hist=False)
figure.add_trace(go.Scatter(x = [mean,mean], y = [0,1.4], mode = "lines", name = "mean"))
figure.add_trace(go.Scatter(x = [mean_of_sample_2,mean_of_sample_2],y = [0,1.4],mode = "lines",name = "Mean of students who were given extra classes"))
figure.show()

z_score = (mean - mean_of_sample_2)/std_deviation
print("The z score is", z_score)