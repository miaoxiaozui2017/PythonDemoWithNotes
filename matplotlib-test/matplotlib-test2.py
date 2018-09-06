#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

## - 散点图Scatter
## 1.生成数据集
#n = 1024    # data size
#X = np.random.normal(0,1,n) # 每一个点的X值
#Y = np.random.normal(0,1,n) # 每一个点的Y值
#T = np.arctan2(Y,X) # for color value
## 2.显示散点
#plt.scatter(X,Y,s=75,c=T,alpha=.5)  # X,Y:作为location，size：75？，c:颜色为T，color map：默认值None，透明度alpha：50%
#plt.xlim(-1.5,1.5)  # x轴显示范围
#plt.xticks(())  # ignore xticks # 隐藏x轴
#plt.ylim(-1.5,1.5)
#plt.yticks(())  # ignore yticks # 隐藏y轴
#plt.show()

## - 柱状图Bar
## 1.生成数据集
#n = 12
#X = np.arange(n)
#Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
#Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
## 2.柱状图
#plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')  # facecolor：设置主体颜色，edgecolor：设置边框颜色为白色
#plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')
#plt.xlim(-.5,n)
#plt.xticks(())
#plt.ylim(-1.25,1.25)
#plt.yticks(())
## 3.添加数据
#for x,y in zip(X,Y1):
#    # ha:horizontal alignment
#    # va:vertical alignment
#    plt.text(x+0.4,y+0.05,'%.2f' % y,ha='center',va='bottom')
#for x,y in zip(X,Y2):
#    # ha:horizontal alignment
#    # va:vertical alignment
#    plt.text(x+0.4,-y-0.05,'%.2f' % y,ha='center',va='top')
#plt.show()

## - 等高线图Contours
## 1.生成数据集
#def f(x,y):
#    # the height function
#    return (1-x/2+x**5+y**3)*np.exp(-x**2,-y**2)
#n = 256
#x = np.linspace(-3,3,n)
#y = np.linspace(-3,3,n)
#X,Y = np.meshgrid(x,y)  # 在二维平面中将每一个x和每一个y分别对应起来，编织成栅格
#plt.xticks(())
#plt.yticks(())
## 2.填充颜色
## use plt.contourf to filling contours
## X, Y and value for (X,Y) point
#plt.contourf(X,Y,f(X,Y),8,alpha=.75,cmap=plt.cm.hot) # 透明度0.75，颜色对应到color map的暖色组
## 3.绘制等高线
## use plt.contour to add contour lines
#C = plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5)    # 8:代表等高线的密集程度（0：图像一分为二），颜色选黑色，线宽选0.5    
## 4.添加高度数字
#plt.clabel(C,inline=True,fontsize=10)   # inline：控制是否将label画在线里面
#plt.show()

## - 图片Image
## 1.生成数据集
#a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
#    0.365348418405, 0.439599930621, 0.525083754405,
#    0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
## 3x3的2D-array来表示点的颜色，每一个点就是一个pixel
#plt.xticks(())
#plt.yticks(())
## 2.画出图片
#plt.imshow(a,interpolation='nearest',cmap='bone',origin='lower')    # color map可直接用'bone'传入参数，origin： 代表选择的原点的位置,interpolation：这里使用的是内插法中的Nearest-neighbor
## 3.colorbar
#plt.colorbar(shrink=.92)    # shrink：使colorbar的长度变短为原来的92%
#plt.show()

# - 3D数据
# 1.导入Axes 3D模块
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()  # 先定义一个图像窗口
ax = Axes3D(fig)    # 在窗口上添加3D坐标轴
# 2.生成数据集
# X, Y value
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)  # x-y平面的网格
R = np.sqrt(X**2+Y**2)
# height value
Z = np.sin(R)
# 3.abs画出三维曲面
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow')) # 颜色：rainbow，rstride：代表row的跨度，cstride：代表column的跨度，此跨度取1
# ax.plot_surface(X,Y,Z,rstride=5,cstride=5,cmap=plt.get_cmap('rainbow')) # 此跨度取5
# 4.添加投影
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap=plt.get_cmap('rainbow'))  # zdir：决定投影面
plt.show()
