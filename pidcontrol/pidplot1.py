import control
import matplotlib.pyplot as plt
import numpy
import os, time, glob

def pidplot1(num,den,kp,ki,kd):
    G = control.tf(num,den)
    if ki!=0:
        g2=control.tf([kd,kp,ki],[1,0])
    else:
        g2=control.tf([kd,kp],[1])
    k=control.series(G,g2)
    v = control.feedback(k,1)
    t1,y1 =control.step_response(G)
    t2,y2=control.step_response(v)
    plt.plot(t2,y2,'r',linewidth=1,label='G(s) with PID control')
    plt.grid(True)
    s='(Kp='+str(kp)+',Ki='+str(ki)+',Kd='+str(kd)+')'
    plt.title('Time response of G(s) with PID control'+s)
    plt.xlabel('Time(sec)')
    plt.ylabel('Amplitude')
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', 'pidcontrol', 'pidc1.png')):
            os.remove(filename)

    pidc1=os.path.join('static', 'pidcontrol', 'pidc1.png')
    plt.savefig(pidc1)
    plt.clf()
    plt.cla()
    plt.close()
    return pidc1