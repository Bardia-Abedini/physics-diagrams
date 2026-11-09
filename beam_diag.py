import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams['font.family']='serif'; plt.rcParams['font.serif']=['Liberation Serif','DejaVu Serif']; plt.rcParams['mathtext.fontset']='stix'
fig,ax=plt.subplots(figsize=(7.2,3.6),dpi=200); ax.axis('off')
ax.add_patch(Rectangle((0,0),100,2.2,fill=False,lw=1.6))
ax.text(0,3.0,'0 cm',ha='center',fontsize=9); ax.text(100,3.0,'100 cm',ha='center',fontsize=9)
def up(x,lab): 
    ax.annotate('',xy=(x,15),xytext=(x,2.2),arrowprops=dict(arrowstyle='-|>',lw=1.6,color='k'))
    ax.text(x+1.2,12.5,lab,fontsize=11)
def down(x,lab,L=12,dx=1.2):
    ax.annotate('',xy=(x,-L),xytext=(x,0),arrowprops=dict(arrowstyle='-|>',lw=1.6,color='k'))
    ax.text(x+dx,-L+0.5,lab,fontsize=10)
up(30,r'$F_4$ (scale A)'); up(80,r'$F_5$ (scale B)')
down(17.8,r'$m_Ag + m_{clip}g$',10); down(49.3,r'$m_{stick}g$ (c.m.)',12); down(76.75,r'$m_Bg + m_{clip}g$',10,1.2)
down(30,'',4.5,0); down(80,'',4.5,0)
ax.text(31,-4.8,'clip',fontsize=8); ax.text(81,-4.8,'clip',fontsize=8)
rows=[(17.8,r'$l_2$',-15),(30,r'$l_4$',-18),(49.3,r'$l_1$',-21),(76.75,r'$l_3$',-24),(80,r'$l_5$',-27)]
for x,l,y in rows:
    ax.annotate('',xy=(x,y),xytext=(0,y),arrowprops=dict(arrowstyle='->',lw=0.8))
    ax.plot([x,x],[y-0.8,y+0.8],color='k',lw=0.8)
    ax.text(x+1,y-0.4,l,fontsize=11,va='center')
ax.plot([0,0],[-28,0],color='k',lw=0.6,ls=':')
ax.text(-1,-12,'pivot\n(0 cm end)',ha='right',fontsize=8,va='center')
ax.set_xlim(-12,112); ax.set_ylim(-29,17)
fig.tight_layout(); fig.savefig('beam_fbd.png',bbox_inches='tight')
