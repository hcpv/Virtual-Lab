import numpy as np
from scipy import signal
import control
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import os, time, glob

def compute(num,den):
    """Return filename of plot of the damped_vibration function."""
    print (os.getcwd())
    num=list(map(int,num.split()))
    den=list(map(int,den.split()))
    sys = signal.TransferFunction(num,den)
    tf=control.tf(num,den)
    t1,y1 = signal.step(sys)
    t2,y2=signal.impulse(sys)
    s=str(tf)
    s=s.split('\n')
    s1='('+s[1].strip()+')'
    s2='('+s[3].strip()+')'
    plt.title('Time Response of H(s)='+s1+'/'+s2)
    plt.plot(t1,y1,'b--',linewidth=3,label='Step Response')
    plt.plot(t2,y2,'r',linewidth=3,label='Impulse Response')
    plt.xlabel('Time')
    plt.ylabel('Response (y)')
    plt.legend(loc='best')
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', 'Plot1.png')):
            os.remove(filename)
    plotfile = os.path.join('static', 'Plot1'+ '.png')
    plt.savefig(plotfile)
    plt.clf()
    plt.cla()
    plt.close()
    return plotfile
    

