"""
作者：ZYC
时间：2021年09月21日
"""

import matplotlib.pyplot as plt
# 模块plt包含绘制图表的函数
import matplotlib

# 解决matplotlib不能输出中文问题
matplotlib.rc("font", family = 'LiSu')
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('ggplot')
fig, ax = plt.subplots()  # 函数subplots在图片fig上绘制多个图表（ax）
ax.plot(input_values, squares, linewidth = 3)  # 方法plot在图表ax上根据数据绘制折线图
ax.set_title("平方数", fontsize = 20)
ax.set_xlabel("值", fontsize = 10)
ax.set_ylabel("值的平方", fontsize = 10)
ax.tick_params(axis = 'both', labelsize = 10)

plt.show()  # 打开Matplotlib查看器并显示图表
