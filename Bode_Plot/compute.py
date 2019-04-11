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
    s=str(tf)
    s=s.split('\n')
    s1='('+s[1].strip()+')'
    s2='('+s[3].strip()+')'
    w,mag,phase=signal.bode(sys)
    plt.subplot(2,1,1)
    plt.semilogx(w,mag,'b',linewidth=3)
    plt.xlabel('Frequency(rad/sec)')
    plt.ylabel('Magnitude-dB')
    plt.title('Bode plot of H(s)='+s1+'/'+s2+'\nMagnitude Plot')
    plt.subplot(2,1,2)
    plt.semilogx(w,phase,'r',linewidth=3)
    plt.xlabel('Frequency(rad/sec)')
    plt.ylabel('Phase-dB')
    plt.title('Phase Plot')  
    plt.subplots_adjust(hspace=0.8) 
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', 'Plot.png')):
            os.remove(filename)
    plotfile = os.path.join('static', 'Plot' + '.png')
    plt.savefig(plotfile)
    plt.clf()
    plt.cla()
    plt.close()
    return plotfile
    

