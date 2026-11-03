# Minimal QR encoder (byte mode, ECC M, versions 1-6) -> SVG
import sys
EC={1:(10,[(1,16)]),2:(16,[(1,28)]),3:(26,[(1,44)]),4:(18,[(2,32)]),5:(24,[(2,43)]),6:(16,[(4,27)])}
AL={1:[],2:[6,18],3:[6,22],4:[6,26],5:[6,30],6:[6,34]}
EXP=[0]*512;LOG=[0]*256;x=1
for i in range(255):
    EXP[i]=x;LOG[x]=i;x<<=1
    if x&256:x^=0x11d
for i in range(255,512):EXP[i]=EXP[i-255]
def mul(a,b): return 0 if a==0 or b==0 else EXP[LOG[a]+LOG[b]]
def gen(n):
    g=[1]
    for i in range(n):
        ng=[0]*(len(g)+1)
        for j,c in enumerate(g):
            ng[j]^=c; ng[j+1]^=mul(c,EXP[i])
        g=ng
    return g
def ecc(data,n):
    g=gen(n);r=list(data)+[0]*n
    for i in range(len(data)):
        c=r[i]
        if c:
            for j in range(len(g)):r[i+j]^=mul(g[j],c)
    return r[len(data):]
def encode(text):
    b=text.encode()
    for v in range(1,7):
        ecn,blocks=EC[v];cap=sum(c*d for c,d in blocks)
        if len(b)+2<=cap:break
    bits=[]
    def put(val,n):
        for i in range(n-1,-1,-1):bits.append((val>>i)&1)
    put(4,4);put(len(b),8)
    for c in b:put(c,8)
    put(0,min(4,cap*8-len(bits)))
    while len(bits)%8:bits.append(0)
    data=[int(''.join(map(str,bits[i:i+8])),2) for i in range(0,len(bits),8)]
    pad=[0xEC,0x11];k=0
    while len(data)<cap:data.append(pad[k%2]);k+=1
    blks=[];i=0
    for cnt,dl in blocks:
        for _ in range(cnt):blks.append(data[i:i+dl]);i+=dl
    ecs=[ecc(bl,ecn) for bl in blks]
    final=[]
    for j in range(max(len(bl) for bl in blks)):
        for bl in blks:
            if j<len(bl):final.append(bl[j])
    for j in range(ecn):
        for e in ecs:final.append(e[j])
    n=17+4*v
    M=[[None]*n for _ in range(n)]
    def finder(r,c):
        for dr in range(-1,8):
            for dc in range(-1,8):
                rr,cc=r+dr,c+dc
                if 0<=rr<n and 0<=cc<n:
                    on=(0<=dr<=6 and dc in(0,6)) or (0<=dc<=6 and dr in(0,6)) or (2<=dr<=4 and 2<=dc<=4)
                    M[rr][cc]=1 if on else 0
    finder(0,0);finder(0,n-7);finder(n-7,0)
    for i in range(8,n-8):M[6][i]=M[i][6]=1 if i%2==0 else 0
    for r in AL[v]:
        for c in AL[v]:
            if M[r][c] is not None:continue
            for dr in range(-2,3):
                for dc in range(-2,3):
                    M[r+dr][c+dc]=1 if max(abs(dr),abs(dc))!=1 else 0
    M[n-8][8]=1
    res=[[M[r][c] is not None for c in range(n)] for r in range(n)]
    for i in range(9):
        res[8][i]=res[i][8]=True
    for i in range(8):
        res[8][n-1-i]=res[n-1-i][8]=True
    allbits=[]
    for byte in final:
        for i in range(7,-1,-1):allbits.append((byte>>i)&1)
    D=[[M[r][c] if M[r][c] is not None else 0 for c in range(n)] for r in range(n)]
    pos=[];col=n-1;up=True
    while col>0:
        if col==6:col-=1
        rows=range(n-1,-1,-1) if up else range(n)
        for r in rows:
            for c in (col,col-1):
                if not res[r][c]:pos.append((r,c))
        up=not up;col-=2
    for k,(r,c) in enumerate(pos):D[r][c]=allbits[k] if k<len(allbits) else 0
    masks=[lambda r,c:(r+c)%2==0,lambda r,c:r%2==0,lambda r,c:c%3==0,lambda r,c:(r+c)%3==0,
           lambda r,c:(r//2+c//3)%2==0,lambda r,c:(r*c)%2+(r*c)%3==0,lambda r,c:((r*c)%2+(r*c)%3)%2==0,
           lambda r,c:((r+c)%2+(r*c)%3)%2==0]
    def fmt(mask):
        d=(0<<3)|mask  # M=00
        v_=d<<10
        for i in range(14,9,-1):
            if v_&(1<<i):v_^=0x537<<(i-10)
        return ((d<<10)|v_)^0x5412
    def apply(mask):
        G=[row[:] for row in D]
        for r,c in pos:
            if masks[mask](r,c):G[r][c]^=1
        f=fmt(mask)
        fb=[(f>>i)&1 for i in range(15)]  # bit i
        # around top-left
        coords1=[(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,7),(8,8),(7,8),(5,8),(4,8),(3,8),(2,8),(1,8),(0,8)]
        coords2=[(n-1,8),(n-2,8),(n-3,8),(n-4,8),(n-5,8),(n-6,8),(n-7,8),(8,n-8),(8,n-7),(8,n-6),(8,n-5),(8,n-4),(8,n-3),(8,n-2),(8,n-1)]
        for i in range(15):
            b_=fb[14-i]
            r,c=coords1[i];G[r][c]=b_
            r,c=coords2[i];G[r][c]=b_
        return G
    def penalty(G):
        p=0
        for lines in (G,[list(x) for x in zip(*G)]):
            for row in lines:
                run=1
                for i in range(1,n):
                    if row[i]==row[i-1]:
                        run+=1
                    else:
                        if run>=5:p+=run-2
                        run=1
                if run>=5:p+=run-2
                s=''.join(map(str,row))
                p+=40*(s.count('10111010000')+s.count('00001011101'))
        for r in range(n-1):
            for c in range(n-1):
                if G[r][c]==G[r+1][c]==G[r][c+1]==G[r+1][c+1]:p+=3
        dark=sum(map(sum,G));p+=abs(dark*100//(n*n)-50)//5*10
        return p
    best=min(range(8),key=lambda m:penalty(apply(m)))
    return apply(best)
def svg(G,color='#4A2416',border=2):
    n=len(G);s=n+2*border;path=[]
    for r in range(n):
        for c in range(n):
            if G[r][c]:path.append(f'M{c+border} {r+border}h1v1h-1z')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}" shape-rendering="crispEdges"><path fill="{color}" d="{"".join(path)}"/></svg>'
if __name__=='__main__':
    G=encode(sys.argv[1]);open(sys.argv[2],'w').write(svg(G))
    try:
        from PIL import Image
        import cv2
        n=len(G);im=Image.new('L',((n+8)*10,)*2,255)
        for r in range(n):
            for c in range(n):
                if G[r][c]:
                    im.paste(0,((c+4)*10,(r+4)*10,(c+5)*10,(r+5)*10))
        im.save('qr-check.png')
        print('lido pelo OpenCV:',cv2.QRCodeDetector().detectAndDecode(cv2.imread('qr-check.png'))[0])
    except ImportError:
        print('SVG gerado. (Instale pillow e opencv-python para conferir a leitura automaticamente.)')
