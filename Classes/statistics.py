import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#столбчатые диаграммы по группам вопросов 
sns.catplot(x="группа вопросов", y="количество отвечавших", data=pd.read_csv('Data/Ratings/groupStatistics.sys'), height=6, kind="bar",  hue = 'группа людей')
sns.catplot(x="группа вопросов", y="количество правильных", data=pd.read_csv('Data/Ratings/groupStatistics.sys'), height=6, kind="bar",  hue = 'группа людей')
