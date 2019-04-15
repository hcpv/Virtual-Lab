import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import control
import os, time, glob

def locusplot(num,den):
	G = control.tf(num,den)
	control.root_locus(G)
	s1="("
	s2="("
	s=str(G)
	s=s.split('\n')
	s[1]=s[1].strip()
	s[3]=s[3].strip()
	s1=s1+s[1]+')'
	s2=s2+s[3]+')'
	plt.grid(True)
	plt.title('Root Locus of G(s)='+(s1)+'/'+(s2))
	if not os.path.isdir('static'):
		os.mkdir('static')
	else:
		for filename in glob.glob(os.path.join('static', 'RootLocus','rlp.png')):
			os.remove(filename)
	rlp=os.path.join('static','RootLocus','rlp.png')
	plt.savefig(rlp)
	plt.clf()
	plt.cla()
	plt.close()
	return rlp