import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

locationLabel = 'Charges Laid by Location & Year'
year = '2007'

pio.templates.default = "plotly_white"
data = pd.read_csv("data2.csv")

data2 = data.set_index([locationLabel])[year].nlargest(10).reset_index()  # get top 10 row

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=data2[locationLabel], y=data2[year]
    )
)

buttons = []
for year in data.columns[1:]:
    try:
        data2 = data.set_index([locationLabel])[year].nlargest(10).reset_index()  # get top 10 row
        buttons.append(dict(method='update',
                            label=year,
                            args=[{
                                'x': [data2[locationLabel]],
                                'y': [data2[year].values]
                            }, [0]])
                       )
    except:
        buttons.append(dict(method='update',
                            label=year,
                            args=[{
                                'x': [data[locationLabel]],
                                'y': [data[locationLabel].values.fill(0)]
                            }, [0]])
                       )

updatemenu = []
your_menu = dict()
updatemenu.append(your_menu)
updatemenu[0]['buttons'] = buttons
updatemenu[0]['direction'] = 'down'
updatemenu[0]['showactive'] = True

fig.update_layout(updatemenus=updatemenu)

fig.show()
