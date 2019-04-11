import numpy as np
import control
from PIL import Image,ImageDraw,ImageFont
import matplotlib.pyplot as plt
import os, time, glob

def compute(num,den):
    """Return filename of plot of the damped_vibration function."""
    print (os.getcwd())
    num=list(map(int,num.split()))
    den=list(map(int,den.split()))
    tf=control.tf(num,den)
    image=Image.open('background.png')
    draw=ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=16)
    color='rgb(0,0,0)'
    (x,y)=(23,0)
    roots=np.roots(den)
    s=str(tf)
    s=s.split('\n')
    s1='('+s[1].strip()+')'
    s2='('+s[3].strip()+')'
    s='Roots of the Characteristic Equation of H(s)='+s1+'/'+s2+' :'
    r=[]
    for i in roots:
        r.append(str(i))
    draw.text((x,y),s,font=font,fill=color)
    y=y+17
    for i in r:
        draw.text((x,y),i,font=font,fill=color)
        y=y+17
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', 'Result.png')):
            os.remove(filename)
    plotfile = os.path.join('static', 'Result'+ '.png')
    image.save(plotfile)
    return plotfile
    

