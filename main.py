import json,os,sys,urllib.request as U
E=os.environ['MAKEFUN_ENV_URL']
def F(p,d):return json.load(U.urlopen(E+p,json.dumps(d).encode()))
D={2:(-21,-19,-12,-8,8,12,19,21),3:(-11,-9,9,11),4:(-10,-1,1,10)}
D[5]=D[6]=D[3]+D[4]
C={98:1,91:2,28:4,21:8,95:3,25:12}
def V(t,r,f,g):
 a=min(f,7-f);c=a+min(r,7-r)
 return[0,100+(r*r*(3+4*g)>>2)+(1<r<5 and a>1)*9,300+8*c,315+4*c,495+18*(r==6),890+3*c,g*8*c or(r<1)*(20,26,10,0)[a]-20*r][t]
def Y(g):
 global T
 W=[[V(t,9-i//10,i%10-1,g)for i in range(120)]for t in range(7)]
 T=W[:7]+[[-W[t][(11-i//10)*10+i%10]for i in range(120)]for t in(6,5,4,3,2,1)]
def att(b,i,c):
 for d in D[2]:
  if b[i+d]==-2*c:return 1
 for d in D[5]:
  j=i+d
  if b[j]==-6*c:return 1
  while b[j]==0:j+=d
  x=-b[j]*c
  if x==5 or x==3+(d*d in(1,100)):return 1
 return-c in(b[i-10*c-1],b[i-10*c+1])
def gen(P,c,q):
 b,s,e,k=P;m=[]
 for i in range(21,99):
  p=b[i]*c
  if not 0<p<7:continue
  if p==1:
   j=i-10*c
   if b[j]==0:
    if not q or j<29 or j>90:m.append((i,j))
    if not q and(i>80 if c>0 else i<39)and b[j-10*c]==0:m.append((i,j-10*c))
   for j in(j-1,j+1):
    if-7<b[j]*c<0 or j==e:m.append((i,j))
   continue
  for d in D[p]:
   j=i
   while 1:
    j+=d;x=b[j]*c
    if x and not-7<x<0:break
    if x or not q:m.append((i,j))
    if x or p in(2,6):break
  if p==6 and not q and i==(95 if c>0 else 25):
   if k&(1 if c>0 else 4)and b[i+1]==b[i+2]==0 and not att(b,i,c)|att(b,i+1,c):m.append((i,i+2))
   if k&(2 if c>0 else 8)and b[i-1]==b[i-2]==b[i-3]==0 and not att(b,i,c)|att(b,i-1,c):m.append((i,i-2))
 return m
def mk(P,c,i,j,n=5):
 b,s,e,k=P;b=b[:];p=b[i];x=b[j]
 s+=T[p][j]-T[p][i]-T[x][j];b[j]=p;b[i]=0;f=0
 k&=~(C.get(i,0)|C.get(j,0))
 if p*c==1:
  if j==e:b[j+10*c]=0;s-=T[-c][j+10*c]
  if abs(j-i)==20:f=(i+j)//2
  if j<29 or j>90:b[j]=n*c;s+=T[n*c][j]-T[p][j]
 if p*c==6 and abs(j-i)==2:
  r,t=(j+1,j-1)if j>i else(j-2,j+1)
  b[t]=b[r];b[r]=0;s+=T[b[t]][t]-T[b[t]][r]
 return b,s,f,k
M=99999
def S(P,c,d,a,B,h,N=1):
 global n
 n+=1
 if n>L:1/0
 b=P[0];z=hash(tuple(b))*c
 if h and z in R:return 0
 I=att(b,b.index(6*c),c)
 if I:d=max(d,0)+1
 q=d<1;bm=None;a0=a
 if q:
  v=c*P[1]
  if v>=B:return v
  a=max(a,v);o=v
 else:
  o=-M;t=H.get(z)
  if t:
   bm=t[3]
   if t[0]>=d and h:
    v=t[1]
    if t[2]==0 or t[2]>0 and v>=B or t[2]<0 and v<=a:return v
  if N and not I and d>2 and c*P[1]>=B:
   v=-S((b,P[1],0,P[3]),-c,d-3,-B,1-B,h+1,0)
   if v>=B:return v
 m=gen(P,c,q);k=K.get(h,())
 m.sort(key=lambda t:(t==bm)*99+(b[t[1]]and abs(b[t[1]])*8-abs(b[t[0]])or(t in k)*6),reverse=1)
 R.add(z);l=0
 for t in m:
  Q=mk(P,c,*t)
  if att(Q[0],Q[0].index(6*c),c):continue
  l+=1
  if q:v=-S(Q,-c,0,-B,-a,h+1)
  else:
   r=1+(d>2 and l>3 and not b[t[1]])
   v=-S(Q,-c,d-r,-a-1,-a,h+1)if l>1 else B
   if v>a:v=-S(Q,-c,d-1,-B,-a,h+1)
  if v>o:o=v;bm=t
  if v>a:a=v
  if a>=B:
   if not b[t[1]]:K[h]=(t,k[0])if k else(t,)
   break
 R.discard(z)
 if q:return o
 if not l:return-M+h if I else 0
 H[z]=(d,o,(o>=B)-(o<=a0),bm)
 return o
def sq(s):return ord(s[0])+4-10*int(s[1])
def uc(i):return chr(i%10+96)+str(10-i//10)
def think(g):
 global n,L,R,K
 b=[7]*120
 for r,w in enumerate(g['start_fen'].split()[0].split('/')):
  w=''.join(' '*int(x)if x<'A'else x for x in w)
  for f,x in enumerate(w):v=' PNBRQKpnbrqk'.find(x);b[21+10*r+f]=v if v<7 else 6-v
 Y(0);P=(b,0,0,15);c=1;R=set()
 for u in g['moves']:
  P=mk(P,c,sq(u),sq(u[2:]),'  nbrq'.find(u[4:]or'q'));c=-c;R.add(hash(tuple(P[0]))*c)
 b=P[0];Y(sum((0,0,1,1,2,4,0,0)[abs(x)]for x in b)<9)
 P=(b,sum(T[x][i]for i,x in enumerate(b)if x!=7),P[2],P[3])
 n=0;L=NODES;K={};z=hash(tuple(b))*c;mv=None
 if len(H)>4e5:H.clear()
 try:
  for d in range(1,64):
   S(P,c,d,-M,M,0);mv=H[z][3]
   if n>L*.4:break
 except:pass
 u=mv and uc(mv[0])+uc(mv[1])
 l=g['legal_moves']
 return u if u in l else u+'q'if u and u+'q'in l else l[0]
NODES=int(os.environ.get('NODES',30000));H={}
while 1:
 g=F('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':g=F('/move',{'game':g['game'],'move':think(g)})
 print(g['game'],g['opponent'],g['outcome'],g['reason'],file=sys.stderr)
