import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#столбчатые диаграммы по группам вопросов 
sns.catplot(x="группа вопросов", y="количество отвечавших", data=pd.read_csv('../Data/Ratings/groupStatistics.sys',sep=";"), height=6, kind="bar",  hue = 'группа людей')
sns.catplot(x="группа вопросов", y="количество правильных", data=pd.read_csv('../Data/Ratings/groupStatistics.sys',sep=";"), height=6, kind="bar",  hue = 'группа людей')

#круговые диаграммы с оценками по группам вопросов (отдельно для каждой группы, здесь только математика)
df_users = pd.read_csv('../Data/Ratings/groupStatistics.sys',sep=";")
df = df_users.groupby('математика').size().reset_index(name='логин')

fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi= 80)

data = df['логин']
categories = df['математика']


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}% ({:d} )".format(pct, absolute)

wedges, texts, autotexts = ax.pie(data,
                                  autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), 
                                  colors=plt.cm.Dark2.colors,
                                startangle=140,
                                 wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"},
                                 shadow=True)

ax.legend(wedges, categories, title="Оценки", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

