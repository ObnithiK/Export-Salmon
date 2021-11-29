# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:43:12 2021

@author: obnit
"""

import pandas as pd , matplotlib.pyplot as plt , numpy as np 

df = pd.read_csv('Export/tested.csv')
df.Date = pd.to_datetime(df.Date)
df.set_index('Date', inplace=True)
df = df.resample('MS').sum()
df['Percent'] = ((df['Positive']/df['Negative'])*100)


df1 = pd.read_csv('Export/reported.csv')
df1.Date = pd.to_datetime(df1.Date)
df1.set_index('Date', inplace=True)
df1 = df1.resample('MS').sum()
df1['Cumulative cases'] = df1["New cases"].cumsum()

df2 = pd.read_csv('Export/export_price.csv')
df2.Date = pd.to_datetime(df2.Date)
df2.set_index('Date', inplace=True)
df2 = df2.resample('MS').sum()

df3 = pd.read_csv('Export/export_weight.csv')
df3.Date = pd.to_datetime(df3.Date)
df3.set_index('Date', inplace=True)
df3 = df3.resample('MS').sum()

labels1 = np.array(df.index)
x1 = np.arange(labels1.size)
y1 = df['Negative']
y2 = df['Positive']
y3 = df['Percent']
fig, ax1 = plt.subplots(figsize=(12, 8))
ax1.bar(x1,y1,color="forestgreen", label="Negative")
ax1.tick_params("y", colors="forestgreen")
ax1.set_ylabel("Number of tested person",color="forestgreen",fontsize=12)
ax1.bar(x1,y2,color="Black", label ="Positive")
ax1.set_xticks(x1)
ax1.set_xticklabels(labels1, rotation = 0)
ax2 = ax1.twinx()
ax2.plot(x1,y3,marker="o", color ="Red",label='Percent')
ax2.tick_params("y", colors="Red")
ax2.set_ylabel("Percent",color="Red",fontsize=12)
ax1.legend(loc="upper left")
ax2.legend(loc="upper center")
ax1.set_title('Number of tested person (Monthly)')
ax1.set_xlabel("Date",color='Black',fontsize=12)
def line_format(label):
    month = label.month_name()[:3]
    if month == 'Jan':
        month += f'\n{label.year}'
    return month
ax1.set_xticklabels(map(line_format, df.index))
plt.show()

labels2 = np.array(df1.index)
x2 = np.arange(labels2.size)
z1 = df1['Cumulative cases']
z2 = df1['New cases']
fig, zx1 = plt.subplots(figsize=(12, 8))
zx1.bar(x2,z2,color='midnightblue', label="New cases")
zx1.tick_params("y", colors="midnightblue")
zx1.set_ylabel("New cases",color="midnightblue",fontsize=12)
zx1.set_xticks(x2)
zx1.set_xticklabels(labels2, rotation = 0)
zx1.set_xlabel("Date",color='Black',fontsize=12)
zx2 = zx1.twinx()
zx2.plot(x2,z1,marker='o', color="Red", label="Cumulative cases")
zx2.tick_params("y", colors="Red")
zx2.set_ylabel("Cumulative cases",color="Red",fontsize=12)
zx1.set_title('Number of cases (Monthly)')
zx1.legend(loc="upper left")
zx2.legend(loc="upper center")
def line_format(label):
    month = label.month_name()[:3]
    if month == 'Jan':
        month += f'\n{label.year}'
    return month
zx1.set_xticklabels(map(line_format, df1.index))
plt.show()

labels3 = np.array(df2.index)
x3 = np.arange(labels3.size)
c1 = df2['PricePerKilo']
fig, q1 = plt.subplots(figsize=(15, 5))
plt.bar(x3,c1,color='gold')
plt.ylabel("PricePerKilo (NOK)")
plt.xticks(x3,labels3, rotation = 0)
plt.title('PricePerkilo (Monthly)')
q1.set_xlabel("Date",color='Black',fontsize=12)
def line_format(label):
    month = label.month_name()[:3]
    if month == 'Jan':
        month += f'\n{label.year}'
    return month
q1.set_xticklabels(map(line_format, df2.index))
plt.show()

labels4 = np.array(df3.index)
x4 = np.arange(labels4.size)
v1 = df3['Weight']
fig, w1 = plt.subplots(figsize=(15, 5))
plt.bar(x4,v1,color='darkorange')
plt.ylabel("Weight (tonnes)")
plt.xticks(x3,labels3, rotation = 0)
plt.title('Export Weight (Monthly)')
w1.set_xlabel("Date",color='Black',fontsize=12)
def line_format(label):
    month = label.month_name()[:3]
    if month == 'Jan':
        month += f'\n{label.year}'
    return month
w1.set_xticklabels(map(line_format, df3.index))
plt.show()

sep_weight1 =df3.iloc[15:34]
sep_weight2 = df3.iloc[13:34]

df['total'] = df['Negative']+df['Positive']
compare1 = np.array(df.index)
x5 = np.arange(compare1.size)
fig, y1 = plt.subplots(figsize=(12, 5))
b1 = df['total']
b2 = sep_weight1['Weight']
plt.bar(x5,b1,color='forestgreen',label="tested total")
plt.bar(x5,b2,color='orange',label="weight")
plt.tick_params("y", colors="maroon")
plt.ylabel('weight & tested total', color = 'maroon')
plt.xticks(x5,compare1, rotation = 0)
plt.title('A comparison of weight and number of tested total')
plt.legend(loc="upper left")
y1.set_xlabel("Date",color='Black',fontsize=12)
def line_format(label):
    month = label.month_name()[:3]
    if month == 'Jan':
        month += f'\n{label.year}'
    return month
y1.set_xticklabels(map(line_format, df.index))
plt.show()

compare2 = np.array(df1.index)
x6 = np.arange(compare2.size)
n1 = df1['New cases']
n2 = sep_weight2['Weight']
fig, nx1 = plt.subplots(figsize=(12, 5))
nx1.bar(x6,n1,color='midnightblue',label="New cases")
nx1.tick_params("y", colors="midnightblue")
nx1.set_ylabel("New cases",color="midnightblue",fontsize=12)
nx1.set_xticks(x6)
nx1.set_xticklabels(compare2, rotation = 0)
nx2 = nx1.twinx()
nx2.plot(x6,n2,marker='o',color='red',label="Weight(tonnes)")
nx2.tick_params("y", colors="Red")
nx2.set_ylabel("Weight(tonnes)",color="Red",fontsize=12)
nx1.set_title('A comparison of weight and new cases')
nx1.legend(loc="upper right")
nx2.legend(loc="upper left")
nx1.set_xlabel("Date",color='Black',fontsize=12)
def line_format(label):
    month = label.month_name()[:3]
    if month == 'Jan':
        month += f'\n{label.year}'
    return month
nx1.set_xticklabels(map(line_format, df1.index))
plt.show()





