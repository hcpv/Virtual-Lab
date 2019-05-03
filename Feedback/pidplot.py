import control
import matplotlib.pyplot as plt
import numpy
import os, time, glob

def pidplot(nlg,dlg,nlh,dlh):
    G = control.tf(nlg,dlg)
    s1="("
    s2="("
    s=str(G)
    s=s.split('\n')
    s[1]=s[1].strip()
    s[3]=s[3].strip()
    s1=s1+s[1]+')'
    s2=s2+s[3]+')'
    t1,y1 =control.step_response(G)
    plt.plot(t1,y1,'b',linewidth=1,label='G(s)')
    plt.grid(True)
    plt.title('Time response of G(s)='+(s1)+'/'+(s2))
    plt.xlabel('Time(sec)')
    plt.ylabel('Amplitude')
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', 'Feedback','pidc.png')):
            os.remove(filename)

    pidc=os.path.join('static', 'Feedback' ,'pidc.png')
    plt.savefig(pidc)
    plt.clf()
    plt.cla()
    plt.close()
    return pidc