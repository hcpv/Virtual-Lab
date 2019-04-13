import control
import matplotlib.pyplot as plt
import numpy
import os, time, glob

def pidplot(num,den,kp,ki,kd):
    G = control.tf(num,den)
    if ki!=0:
        g2=control.tf([kd,kp,ki],[1,0])
    else:
        g2=control.tf([kd,kp],[1])
    k=control.series(G,g2)
    s1="("
    s2="("
    s=str(G)
    s=s.split('\n')
    s[1]=s[1].strip()
    s[3]=s[3].strip()
    s1=s1+s[1]+')'
    s2=s2+s[3]+')'
    v = control.feedback(k,1)
    t1,y1 =control.step_response(G)
    t2,y2=control.step_response(v)
    plt.plot(t1,y1,'b',linewidth=1,label='G(s)')
    plt.grid(True)
    plt.title('Time response of G(s)='+(s1)+'/'+(s2))
    plt.xlabel('Time(sec)')
    plt.ylabel('Amplitude')
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', 'pidcontrol','pidc.png')):
            os.remove(filename)

    pidc=os.path.join('static', 'pidcontrol' ,'pidc.png')
    plt.savefig(pidc)
    plt.clf()
    plt.cla()
    plt.close()
    return pidc