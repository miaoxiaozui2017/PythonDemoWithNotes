#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# 动画Animation
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
# 1.准备工作
fig,ax = plt.subplots()
x = np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))
# 2.构造自定义动画函数
def animate(i):
    '''
    用来更新每一帧上各个x对应的y坐标值，参数表示第i帧
    '''
    line.set_ydata(np.sin(x + i/10.0))
    return line,
# 3.构造开始帧函数
def init():
    line.set_ydata(np.sin(x))
    return line,
# 4.参数设置
ani = animation.FuncAnimation(fig=fig,# fig：进行动画绘制的figure
        func=animate,# func：自定义动画函数，即传入刚定义的函数animate
        frames=100,# frames：动画长度，一次循环包含的帧数
        init_func=init,# init_func：自定义开始帧，即传入刚定义的函数init
        interval=20,# interval：更新频率，以ms计
        blit=False)# blit：选择更新所有点还是仅更新产生变化的点。应选择True。mac用户只能选False才显示动画？
# 5.展示
plt.show()
# 6.保存：保证安装了ffmpeg或者mencoder，更多参考matplotlib animation api
#ani.save('basic_animation.mp4',fps=30,extra_args=['-vcodec','libx264'])
