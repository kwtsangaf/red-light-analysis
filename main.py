import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"
data = pd.read_csv("data2.csv")

data = data.set_index(['Charges Laid by Location & Year'])['2020'].nlargest(10).reset_index() # get top 10 row
# data = data.sort_values('2020', ascending=False)  # sort all rows by column '2020'

figure = px.bar(data,
                x='Charges Laid by Location & Year',
                y='2020',
                title="Red Light Charges Analysis")
figure.show()
