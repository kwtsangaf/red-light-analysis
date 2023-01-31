import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"

data = pd.read_csv("data2.csv")

figure = px.bar(data,
                x='Charges Laid by Location & Year',
                y='2020',
                title="Red Light Charges Analysis")
figure.show()
