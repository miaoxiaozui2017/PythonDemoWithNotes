#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# test for python code

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)    # 定义范围以及个数
#print(x)
#y = 2*x+1
y=0.1*x
#y1 = 2*x+1
#y2 = x**2

plt.figure()
#plt.figure(num=1,figsize=(8,5),)
#plt.figure(num = 3,figsize = (8,5))    # 单独的小窗口,num编号，figsize大小

# 设置坐标轴-基本
#plt.xlim((-1,2))    # 设置x坐标轴范围
#plt.ylim((-2,3))    # 设置y坐标轴范围
plt.ylim(-2,2)
#plt.xlabel('I am x')    # 设置x坐标轴名称
#new_sticks = np.linspace(-1,2,5)
#plt.xticks(new_sticks)    # 设置x轴刻度
#plt.ylabel('I am y')    # 设置y坐标轴名称
#plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])    # 设置x轴刻度

# 设置坐标轴-修改位置
ax = plt.gca()  # 获取当前坐标轴信息
ax.spines['right'].set_color('none')    # 设置边框，右侧；设置边框颜色：默认白色
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')   # 设置x坐标刻度数字或名称的位置：bottom（所有位置：top、bottom、both、default、none）
ax.spines['bottom'].set_position(('data',0))    # 设置边框位置：y = 0的位置（位置所有属性：outward、axes、data）
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 设置坐标轴-tick能见度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)  # 重新调节字体大小
    # 在plt 2.0.2或更高的版本中，设置zorder给plot在z轴方向排序
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.7,zorder=2)) # bbox：设置目的内容的透明度相关参数:{facecolor：调节box前景色，edgecolor：设置边框（本处设置边框为无），alpha:设置透明度}
# Legend添加图例
#l1,=plt.plot(x,y1,label='linear line')  # l1结尾加逗号：plt.plot()返回的是一个列表
#l2,=plt.plot(x,y2,color = 'red',linewidth = 1.0,linestyle = '--',label='square line')    # color曲线颜色，linewidth线宽，linestyle线型,label图例名称
#plt.legend(loc='upper right')  # loc图例将添加在图中的右上角
#plt.legend(handles=[l1,l2],labels=['up','down'],loc='best') # 'best'：自动分配最佳位置，loc参数:{'best':0,'upper right':1,'upper left':2,'lower left':3,'lower right':4,'right':5,'center left':6,'center right':7,'lower center':8,'upper center':9,'center':10,}

# Annotation标注
#x0 = 1
#y0 = 2*x0 + 1
#plt.plot([x0,x0,],[0,y0,],'k--',linewidth=2.5)
#plt.plot(x,y,)
plt.plot(x,y,linewidth=10,zorder=1) # 在plt 2.0.2或更高的版本中，设置zorder给plot在z轴方向排序
#plt.scatter([x0,],[y0,],s=50,color='b') # 设置点的样式
# 用plt里面的annotation
#plt.annotate(r'$2x+1=%s$' % y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),
#        textcoords='offset points',fontsize=16,
#        arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))
# xycoords='data':基于数据的值来选位置，xytext=(+30,-30):对标注位置的描述，textcoords='offset points':对标注位置的xy偏差值，arrowstyle:对图中箭头类型的设置
# 直接用plt里面的text
#plt.text(-3.7,3,r'$This\ is\ the\ some\ text.\mu\ \sigma_i\ \alpha_t$',
#        fontdict={'size':16,'color':'r'})
# -3.7,3:选取text的位置，\转义符：转义空格，fontdict设置文本字体
plt.show()

