# coding=utf-8
import csv
from datetime import datetime


# filename = 'data/sitka_weather_07-2014.csv'
filename = 'data/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_now = next(reader)

    # 从文件中获取最高温度和日期
    dates, highs, lows = [], [], []
    # for index, column_header in enumerate(header_now):
    #     print(index, column_header)

    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')

    high = int(row[4])
    high = int(row[5])