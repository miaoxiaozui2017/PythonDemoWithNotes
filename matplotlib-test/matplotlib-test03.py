#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import matplotlib.pyplot as plt

## 多合一显示Subplot

## 均匀图中图
## 1.创建一个图像窗口
#plt.figure()
## 2.创建小图，并指定位置
#plt.subplot(2,2,1)  # subplot(2,2,1)来创建小图，表示将整个图像窗口分为2行2列，当前位置为1
#plt.plot([0,1],[0,1])   # 在第1个位置创建一个小图
#plt.subplot(2,2,2)
#plt.plot([0,1],[0,2])
#plt.subplot(223)    # 同subplot(2,2,3)，简写形式
#plt.plot([0,1],[0,3])
#plt.subplot(224)
#plt.plot([0,1],[0,4])
## 3.展示
#plt.show()

## 不均匀图中图
## 1.创建一个图像窗口
#plt.figure()
## 2.创建小图，并指定位置
#plt.subplot(2,1,1)
#plt.plot([0,1],[0,1])
#plt.subplot(2,3,4)  # 位置从4开始计算，因为上面1行占了3列的大小
#plt.plot([0,1],[0,2])
#plt.subplot(235)
#plt.plot([0,1],[0,3])
#plt.subplot(236)
#plt.plot([0,1],[0,4])
## 3.展示
#plt.show()

## 分格显示Subplot
## 三种方法！
## 一、subplot2grid
## 1.创建一个图像窗口
#plt.figure()
## 2.创建小窗口
#ax1 = plt.subplot2grid((3,3),(0,0),colspan=3)   # subplot2grid((3,3),(0,0),colspan=3):(3,3)表示将整个图像窗口分成3行3列，(0,0)表示从第0行第0列开始作图，colspan=3表示列的跨度为3,rowspan=1表示行的跨度为1，这两个缺省，默认跨度为1
#ax1.plot([1,2],[1,2])   # 画小图
#ax1.set_title('ax1_title')  # 设置小图的标题
#ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)
#ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
#ax4 = plt.subplot2grid((3,3),(2,0))
#ax5 = plt.subplot2grid((3,3),(2,1))
#ax4.scatter([1,2],[2,2])
#ax4.set_xlabel('ax4_x')
#ax4.set_ylabel('ax4_y')
## 3.展示
#plt.show()
## 二、gridspec
#import matplotlib.gridspec as gridspec
## 1.创建一个图像窗口
#plt.figure()
#gs = gridspec.GridSpec(3,3) # 将整个图像窗口分成3行3列
## 2.创建小窗口
#ax6 = plt.subplot(gs[0,:])  # gs[0,:]表示这个图占第0行和所有列
#ax7 = plt.subplot(gs[1,:2]) # gs[1,:2]表示这个图占第1行和第2列前的所有列
#ax8 = plt.subplot(gs[1:,2]) # gs[1:,2]表示这个图占第1行后的所有行和第2列
#ax9 = plt.subplot(gs[-1,0]) # gs[-1,0]表示这个图占倒数第1行和第0列
#ax10 = plt.subplot(gs[-1,-2])   # gs[-1,-2]表示这个图占倒数第1行和倒数第2列
## 3.展示
#plt.show()
## 三、subplots
## 1.创建一个图像窗口
## 2.创建小窗口
#f,((ax11,ax12),(ax13,ax14)) = plt.subplots(2,2,sharex=True,sharey=True) # 先创建一个2行2列的图像窗口，sharex=True表示共享x轴坐标，sharey=True表示共享y轴坐标，从左到右从上到小依次ax11->ax14
#ax11.scatter([1,2],[1,2])
#plt.tight_layout()  # 表示紧凑显示图像
## 3.展示
#plt.show()

## 图中图plot in plot
## 1.准备图像窗口和数据
## 初始化figure
#fig = plt.figure()
## 创建数据
#x = [1,2,3,4,5,6,7]
#y = [1,3,4,2,5,8,6]
## 2.绘制大图
#left,bottom,width,height = 0.1,0.1,0.8,0.8  # 4个值都是占整个figure坐标系的百分比
## 将大图坐标系添加到figure中，颜色为r(red)，取名为title
#ax1 = fig.add_axes([left,bottom,width,height])
#ax1.plot(x,y,'r')
#ax1.set_xlabel('x')
#ax1.set_ylabel('y')
#ax1.set_title('title')
## 3.绘制小图
#left,bottom,width,height = 0.2,0.6,0.25,0.25
#ax2 = fig.add_axes([left,bottom,width,height])
#ax2.plot(y,x,'b')
#ax2.set_xlabel('x')
#ax2.set_ylabel('y')
#ax2.set_title('title inside 1')
## 直接往窗口中添加新的坐标系
#plt.axes([0.6,0.2,0.25,0.25])
#plt.plot(y[::-1],x,'g') # 注意对y进行了逆序处理
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('title inside 2')
## 4.展示
#plt.show()

# 次坐标系
# 1.准备工作
import numpy as np
x = np.arange(0,10,0.1)
y1 = 0.05*x**2
y2 = -1*y1  # y1与y2倒置
# 2.画两个y坐标
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()   # 生成镜面效果
ax1.plot(x,y1,'g-') # green,solid line
ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data',color='g')
ax2.plot(x,y2,'b-') # blue
ax2.set_ylabel('Y2 data',color='b')
# 3.展示
plt.show()

