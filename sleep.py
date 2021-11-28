import pandas as pd
import plotly.express as px
df=pd.read_csv("sleep.csv")
sc=px.scatter(df,x='Coffee in ml', y='sleep in hours')
sc.show()
co=df.corr()
print(co)