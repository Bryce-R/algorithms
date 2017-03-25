"""
===========================
Formation animation of 6 quadcopters in triangular formation
===========================
tutorials from : 
https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/ 
"""

from numpy import sin, cos
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
# plt.style.use('ggplot')
# plt.style.use('fivethirtyeight')

## import Tri1Tplg2_data 
Tri1Tplg1_data = sio.loadmat('data/Tri1Tplg1_data.mat')
Tri1Tplg2_data = sio.loadmat('data/Tri1Tplg2_data.mat')

x_r1,k1,n,X1 = Tri1Tplg1_data['x_r'],Tri1Tplg1_data['k'],Tri1Tplg1_data['n'][0][0],Tri1Tplg1_data['X']
x_r2,k2,n,X2 = Tri1Tplg2_data['x_r'],Tri1Tplg2_data['k'],Tri1Tplg2_data['n'][0][0],Tri1Tplg2_data['X']

#print x_r1.shape
#print X1.shape

## sampling interval
dt = 0.05

## First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(figsize=(6.4*2.5, 4.8*2.5))
plt.title('Triangular Formation')
plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
plt.title('Weakly Connected')
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
plt.title('Strongly Connected')
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

## Set axis label 
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax3.set_xlabel('X')
ax3.set_ylabel('Z')
ax4.set_xlabel('X')
ax4.set_ylabel('Z')

ax1.set_xlim3d([-2.0, 9.0])
ax1.set_ylim3d([-2.0, 2.0])
ax1.set_zlim3d([-0.10, 0.35])
ax2.set_xlim3d([-2.0, 9.0])
ax2.set_ylim3d([-2.0, 2.0])
ax2.set_zlim3d([-0.10, 0.10])
ax3.set_xlim([-2.6, 8.5])
ax3.set_ylim([-0.05, 0.35])
ax4.set_xlim([-2.6, 8.5])
ax4.set_ylim([-0.05, 0.35])
ax3.grid()
ax4.grid()

liner1 = [ax1.plot(x_r1[0,0:1], x_r1[1,0:1], x_r1[2,0:1])[0]]
linef1 = [ax1.plot(X1[j,0:1], X1[j+1,0:1], X1[j+2,0:1])[0] for j in xrange(0,X1.shape[0],n)]
lines1 = liner1 + linef1
liner2 = [ax2.plot(x_r2[0,0:1], x_r2[1,0:1], x_r2[2,0:1])[0]]
linef2 = [ax2.plot(X2[j,0:1], X2[j+1,0:1], X2[j+2,0:1])[0] for j in xrange(0,X2.shape[0],n)]
lines2 = liner2 + linef2

lines3 = [ax3.plot([],[],lw=1.5)[0]]+ [ax3.plot([],[],lw=1.5)[0] for j in xrange(0,X2.shape[0],n)]
lines4 = [ax4.plot([],[],lw=1.5)[0]]+[ax4.plot([],[],lw=1.5)[0] for j in xrange(0,X2.shape[0],n)]
## Timer on plot
time_template = 'time = %.1fs'
time_text1 = ax1.text(4, 1.0, 0.34, '')
time_text2 = ax2.text(4, 1.0, 0.1, '')

## animation function.  This is called sequentially
def animate(i,x_r1,X1,x_r2,X2):
	# Plot vehicle 1 in 3D
    lines1[0].set_data(x_r1[0][:i],x_r1[1][:i])
    lines1[0].set_3d_properties(x_r1[2][:i])
    for line,j in zip(lines1[1:], range(0,X1.shape[0],12)):
        line.set_data(X1[j][0:i], X1[j+1][0:i])
        line.set_3d_properties(X1[j+2][0:i])
    # plot vehicle 1 XZ plot
    for line,j in zip(lines3[1:], range(0,X1.shape[0],12)):
        line.set_data(X1[j][0:i], X1[j+2][0:i])

	# Plot vehicle 2 in 3D
    lines2[0].set_data(x_r2[0][:i],x_r2[1][:i])
    lines2[0].set_3d_properties(x_r2[2][:i])
    for line,j in zip(lines2[1:], range(0,X2.shape[0],12)):
        line.set_data(X2[j][0:i], X2[j+1][0:i])
        line.set_3d_properties(X2[j+2][0:i])
    # plot vehicle 2 XZ plot
    for line,j in zip(lines4[1:], range(0,X2.shape[0],12)):
        line.set_data(X2[j][0:i], X2[j+2][0:i])

    time_text1.set_text(time_template % (i*dt))
    time_text2.set_text(time_template % (i*dt))
    return (lines1,lines2,lines3,lines4,time_text1,time_text2)

## call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=np.arange(1, k1),fargs=(x_r1,X1,x_r2,X2), 
                                interval=10, blit=False)

""" 
Uncomment the line below to save this animation in ubuntu 
have to have mencoder installed first 
"""
# anim.save('formation_animation.mp4', writer = 'mencoder', fps=15)

plt.show()
