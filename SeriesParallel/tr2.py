import control
import matplotlib.pyplot as plt
import numpy
import os, time, glob

def tr2(numG,denG,numH,denH):
    G = control.tf(numG,denG)
    H=control.tf(numH,denH)
    k=control.parallel(G,H)
    s1="("
    s2="("
    s=str(k)
    s=s.split('\n')
    s[1]=s[1].strip()
    s[3]=s[3].strip()
    s1=s1+s[1]+')'
    s2=s2+s[3]+')'
    t1,y1=control.step_response(k)
    plt.plot(t1,y1,'b',linewidth=1,label='G(s)')
    plt.grid(True)
    plt.title('Time response of Parallel Operation\n'+(s1)+'/'+(s2))
    plt.xlabel('Time(sec)')
    plt.ylabel('Amplitude')
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', 'SeriesParallel','sp2.png')):
            os.remove(filename)

    sp2=os.path.join('static','SeriesParallel', 'sp2.png')
    plt.savefig(sp2)
    plt.clf()
    plt.cla()
    plt.close()
    return sp2