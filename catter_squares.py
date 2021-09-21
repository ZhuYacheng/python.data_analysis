"""
作者：ZYC
时间：2021年09月21日
"""
import matplotlib.pyplot as plt
import matplotlib

# 解决matplotlib不能输出中文问题
matplotlib.rc("font", family = 'LiSu')

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(2, 4, s = 100)  # 方法scatter在指定位置，和大小绘制单个点
ax.set_title('平方数', fontsize = 20)
ax.set_xlabel('值', fontsize = 15)
ax.set_ylabel('值得平方', fontsize = 15)
ax.tick_params('both', which = 'major', labelsize = 10) # 设置刻度标记大小
plt.show()
