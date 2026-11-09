import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.family']='serif'; plt.rcParams['font.serif']=['Liberation Serif']; plt.rcParams['mathtext.fontset']='stix'
L=np.array([26,49,63,93.]); T=np.array([.46,.63,.78,.99]); T2=T**2
# T vs L
fig,ax=plt.subplots(figsize=(6,4),dpi=200)
c=np.exp(np.polyfit(np.log(L),np.log(T),1)[1]); n=np.polyfit(np.log(L),np.log(T),1)[0]
x=np.linspace(0,100,200); ax.plot(x,c*x**n,'k-',lw=1)
ax.plot(L,T,'o',mfc='none',mec='k',ms=9); ax.plot(L,T,'k.',ms=3)
ax.set_xlim(0,100); ax.set_ylim(0,1.2); ax.set_xlabel('Length of String, L [cm]'); ax.set_ylabel('Period of Revolution, T [s]')
ax.set_title('Period of Revolution vs. Length of String'); ax.grid(True,lw=0.3,color='0.8'); ax.minorticks_on(); ax.grid(True,which='minor',lw=0.2,color='0.9')
fig.tight_layout(); fig.savefig('graph_T_L.png'); plt.close(fig)
# T2 vs L
Lm=L/100; m,b=np.polyfit(Lm,T2,1)
fig,ax=plt.subplots(figsize=(6,4),dpi=200)
x=np.linspace(0.12,1.0,10); ax.plot(x,m*x+b,'k-',lw=1)
ax.plot(Lm,T2,'o',mfc='none',mec='k',ms=9); ax.plot(Lm,T2,'k.',ms=3)
x1,x2=0.30,0.90; y1,y2=m*x1+b,m*x2+b
ax.plot([x1,x2],[y1,y2],'kx',ms=8,mew=1.5)
ax.plot([x1,x2,x2],[y1,y1,y2],'k--',lw=0.8)
ax.text((x1+x2)/2,y1-0.06,f'Δx = {x2-x1:.2f} m',ha='center',fontsize=10)
ax.text(x2+0.01,(y1+y2)/2,f'Δy = {y2-y1:.3f} s²',fontsize=10)
ax.text(0.15,0.95,f'slope = Δy/Δx = {(y2-y1)/(x2-x1):.2f} s²/m',fontsize=10)
ax.set_xlim(0,1.0); ax.set_ylim(0,1.1); ax.set_xlabel('Length of String, L [m]'); ax.set_ylabel('Period Squared, T² [s²]')
ax.set_title('Period Squared vs. Length of String'); ax.grid(True,lw=0.3,color='0.8'); ax.minorticks_on(); ax.grid(True,which='minor',lw=0.2,color='0.9')
fig.tight_layout(); fig.savefig('graph_T2_L.png'); plt.close(fig)
print(n, m, b, y1, y2)
