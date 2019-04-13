import control
import matplotlib.pyplot as plt
import numpy
import os, time, glob

def nqstplot(num,den):
    G = control.tf(num,den) 
    w = numpy.logspace(-3,3,5000)
    control.nyquist(G,w)
    s1="("
    s2="("
    s=str(G)
    s=s.split('\n')
    s[1]=s[1].strip()
    s[3]=s[3].strip()
    s1=s1+s[1]+')'
    s2=s2+s[3]+')'
    plt.grid(True)
    plt.title('Nyquist Diagram of G(s)H(s) = '+(s1)+'/'+(s2))
    plt.xlabel('Re(s)')
    plt.ylabel('Im(s)')

    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', 'NyquistPlot','Plot3.png')):
            os.remove(filename)

    nqst=os.path.join('static','NyquistPlot', 'Plot3.png')
    plt.savefig(nqst)
    plt.clf()
    plt.cla()
    plt.close()
    return nqst
