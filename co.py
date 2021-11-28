import pandas as pd
import plotly.express as px
df=pd.read_csv("sales.csv")
sc=px.scatter(df,x='Temperature', y='Ice-cream Sales( ₹ )')
sc.show()
co=df.corr()
print(co)
