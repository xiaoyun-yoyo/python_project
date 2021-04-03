# coding=utf-8

import plotly.express as px
import pandas as pd

from json_matplotlib.eq_explore_data import lons, mags, titles, lats


data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)
data.head()

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置'
)
fig.write_html('data/global_earthquakes.html')
fig.show()