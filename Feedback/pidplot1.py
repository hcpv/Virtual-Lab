import control
import matplotlib.pyplot as plt
import numpy
import os, time, glob

def pidplot1(nlg,dlg,nlh,dlh):
    G = control.tf(nlg,dlg)
    H = control.tf(nlh,dlh)
    s=str(H)
    s1="("
    s2="("
    s=s.split('\n')
    s[1]=s[1].strip()
    s[3]=s[3].strip()
    s1=s1+s[1]+')'
    s2=s2+s[3]+')'
    v = control.feedback(G,H)
    t2,y2=control.step_response(v)
    plt.plot(t2,y2,'r',linewidth=1,label='G(s) with Feedback H(s)')
    plt.grid(True)
    plt.title('Time response of G(s) with feedback H(s)=G(s)/(1+G(s)H(s))')
    plt.xlabel('Time(sec)')
    plt.ylabel('Amplitude')
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', 'Feedback', 'pidc1.png')):
            os.remove(filename)

    pidc1=os.path.join('static', 'Feedback', 'pidc1.png')
    plt.savefig(pidc1)
    plt.clf()
    plt.cla()
    plt.close()
    return pidc1