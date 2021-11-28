import pandas as pd
import plotly.express as px
df=pd.read_csv("tv.csv")
sc=px.scatter(df,x='Size of TV', y='time')
sc.show()
co=df.corr()
print(co)