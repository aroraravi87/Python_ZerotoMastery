import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import numpy as np
import pandas as pd

def plot1():
    xs= np.linspace(0,10,100)

    #plt.plot(xs,np.sin(xs))
    #plt.plot(xs,np.cos(xs))


    fig=plt.figure()
    ax1=fig.add_subplot(2,2,1)
    ax2=fig.add_subplot(2,2,2)
    ax3=fig.add_subplot(2,2,3)
    ax4=fig.add_subplot(2,2,4)

    #Map1
    ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)

    #Map2
    ax2.scatter(np.arange(20),np.arange(20)+ 3 * np.random.randn(20))
    #map3
    ax3.plot(np.random.randn(30).cumsum(),'k--')

    #Map4
    ax4.plot(np.random.randn(30).cumsum(),'ko-')

    #Display Plot
    plt.show()

def plot2():
    fig,axes=plt.subplots(2,3)
    axes[0,1].plot(np.random.randn(30).cumsum(),'k--')
    axes[1,2].scatter(np.random.randn(20),np.random.randn(20)+3 * np.random.randn(20))
    axes[1,0].scatter(np.arange(10),np.arange(10)+3 * np.random.randn(10))
    plt.show()

"""
'b' - blue
'g' - green
'r' - red
'k' - black
'w' - white


'-' - solid line style
'-' - dashed line style
'-. - dash-dot line style
':' - dotted line style
"""

def plot3():
    xs= np.linspace(0,10,100)
    fig,axes=plt.subplots(1,1)
    axes.set_title("Sin and Cos Comparison")
    axes.plot(xs,np.sin(xs),':r',label="Sin(x)")
    axes.plot(xs,np.cos(xs),'-b',label="Cos(x)")
    axes.legend()
    plt.show()
    
def plot4():
    xs= np.linspace(0,10,100)
    fig,axes=plt.subplots(1,1)
    axes.plot(xs,np.sin(xs),'-r')
    axes.set_xticklabels(["Wake up","Coffee kicks in","Afternoon classes","Coffee Break","party time","Sleepy time"],rotation=45,fontsize="small")
    plt.show()


  ### Matplotlib – Textbox Widgets  

fig,ax= plt.subplots()
fig.subplots_adjust(bottom=0.2)
x=np.arange(-20,20,0.001)
line,=ax.plot(x,np.zeros_like(x),lw=2)
    
def submit(expression):
    ydata=eval(expression)
    line.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

text_box=fig.add_axes([0.1,0.05,0.8,0.075])
text_box=TextBox(text_box,'Evaluate',textalignment='center')
text_box.on_submit(submit)
text_box.set_val("x+20*np.sin(x)")
    
plt.show()
##########Main Calling

#plot1()
#plot2()
#plot3()
#plot4()


