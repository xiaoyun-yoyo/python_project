# coding=utf-8
import csv
import matplotlib.pyplot as plt
from datetime import datetime


# filename = 'data/sitka_weather_07-2014.csv'
filename = 'data/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_now = next(reader)

    # 从文件中获取最高温度和日期
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        dates.append(current_date)
        lows.append(low)

    # 根据最高温度和最低温度绘制图形
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置字体
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 设置图形的格式
    ax.set_title("2014年每日最高温度", fontsize=24)
    ax.set_title("2014年每日最低温度", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    # 绘制倾斜的日期标签
    fig.autofmt_xdate()
    ax.set_ylabel("温度 (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()