# coding=utf-8
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use(['seaborn'])
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置字体
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置图标标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
# 设置每个值坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show()
# 保存图标为图片
plt.savefig('squares_plt.png', bbox_inches='tight')