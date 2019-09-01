#Goal: code that takes in tile number (which is automatically even/odd)
#and placement, and spits out directed connecting points.
#Tile number is (a,b) where a and be are betweeen 0 and 3
#convert to binary to get four bits.
#connecting points are (p,q) numbered 0 to 11. starts upper left
#q increases horizontally. p increases as we move down the page

#then, we compress (p,q) later as 12*(p mod 12) + (q mod 12) to get
#rid of the edges and form a torus.

#For a tiles (a=x,b=y) the connecting points are
# (3x,3y+1) (3x,3y+2) on top. (3x+3,3y+1) (3x+3, 3y+2) bottom.
# (3x+1,3y) (3x+2,3y) on left. (3x+1, 3y+3) (3x+2,3y+3) right.

def tileNum2bitList(n):
    if n == 0:
        return ['0', '0', '0', '0']
    if n==1:
        return ['0', '0', '0', '1']
    b=list(bin(n))
    b[1]='0'
    return b[-4:]

def isOdd(tup):
    return (tup[0]+tup[1]) % 2

def s2nBits(sbits):
    for i in range(4):
        if sbits[i]=='0':
            sbits[i]=0
        if sbits[i]=='1':
            sbits[i]=1
    return sbits  #strings now numbs        

def testAB(bits,x,y):
    if not bits[0] and not bits[1]:
        return (3*x+1, 3*y, 3*x, 3*y+1)
    if not bits[0] and bits[1]:
        return (3*x+1, 3*y, 3*x, 3*y+2)
    if bits[0] and not bits[1]:
        return (3*x+2, 3*y, 3*x, 3*y+1)
    if bits[0] and bits[1]:
        return (3*x+2, 3*y, 3*x, 3*y+2)

def testAD(bits,x,y):
    if not bits[0] and not bits[3]:
        return (3*x+2, 3*y, 3*x+3, 3*y+1)
    if not bits[0] and bits[3]:
        return (3*x+2, 3*y, 3*x+3, 3*y+2)
    if bits[0] and not bits[3]:
        return (3*x+1, 3*y, 3*x+3, 3*y+1)
    if bits[0] and bits[3]:
        return (3*x+1, 3*y, 3*x+3, 3*y+2)    

def testCB(bits,x,y):
    if not bits[1] and not bits[2]:
        return (3*x+1, 3*y+3, 3*x, 3*y+2)
    if not bits[1] and bits[2]:
        return (3*x+2, 3*y+3, 3*x, 3*y+2)
    if bits[1] and not bits[2]:
        return (3*x+1, 3*y+3, 3*x, 3*y+1)
    if bits[1] and bits[2]:
        return (3*x+2, 3*y+3, 3*x, 3*y+1) 
    
def testCD(bits,x,y):
    if not bits[2] and not bits[3]:
        return (3*x+2, 3*y+3, 3*x+3, 3*y+2)
    if not bits[2] and bits[3]:
        return (3*x+2, 3*y+3, 3*x+3, 3*y+1)
    if bits[2] and not bits[3]:
        return (3*x+1, 3*y+3, 3*x+3, 3*y+2)
    if bits[2] and bits[3]:
        return (3*x+1, 3*y+3, 3*x+3, 3*y+1)


def findArcs(tilenum, x, y):
    L=[]
    bits=tileNum2bitList(tilenum)
    bits=s2nBits(bits)
    L.append(testAB(bits,x,y))
    L.append(testAD(bits,x,y))
    L.append(testCB(bits,x,y))
    L.append(testCD(bits,x,y))
    if isOdd((x,y)):
        for i in range(4):
            L[i]=(L[i][2],L[i][3],L[i][0],L[i][1])
            #switch arrow direction
    return L        

def config2matrix(C):
    #C=[[x,x,x,x],[x,x,x,x] etc. 4x4
    L=[]
    for x in range(4):
        for y in range(4):
            L.append(findArcs(C[x][y],x,y))
    #L should have 16 sublists each with four tuples for arcs.
    M=[]
    for i in range(144):
        M.append([0]*144)
    for i in range(16):
        for j in range(4):
            p,q,r,s = L[i][j]
            M[12*(p%12)+(q%12)][12*(r%12)+(s%12)]=1
    return M

def config2dict(C):
    #C=[[x,x,x,x],[x,x,x,x] etc. 4x4
    L=[]
    for x in range(4):
        for y in range(4):
            L.append(findArcs(C[x][y],x,y))
    #L should have 16 sublists each with four tuples for arcs.
    d=dict()
    for i in range(16):
        for j in range(4):
            p,q,r,s = L[i][j]
            d[(p%12,q%12)]=(r%12,s%12)
    return d


def listLoopsInDict(d):
    v=list(d.values())
    v.sort()
    L=[]
    s=[]
    s.append(v.pop(0))
    while len(v):
        while d[s[-1]] in v:
            s.append(v.pop(v.index(d[s[-1]])))
        L.append(s)
        s=[]
        if len(v):
            s.append(v.pop(0))
    return L    
    
def countLoopsInDict(d):
    L=listLoopsInDict(d)
    L2=[]
    for e in L:
        L2.append(len(e))
    return L2    


def loopLengthsInConfig(C):
    d=config2dict(C)
    L=countLoopsInDict(d)
    return L
