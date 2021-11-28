import pandas as pd
import plotly.graph_objects as go
df=pd.read_csv("level.csv")
mean=df.groupby("level")["attempt"].mean()
print (mean)
graph=go.Figure(go.Bar(x=mean,y=["Level 1","Level 2","Level 3","Level 4"],orientation="h"))
graph.show()