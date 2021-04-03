# coding=utf-8
from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


# 创建一个D6
die = Die()

#投几次骰子并把结果存储到一个列表中
results =[]
for roll in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequencie = results.count(value)
    frequencies.append(frequencie)

# 对结果进行可视化
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果'}
y_axis_config ={'title': '结果的频率'}
my_layout = Layout(title='投一个D6 1000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
