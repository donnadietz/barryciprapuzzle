import copy


def FindTokens(L,n,s):
    if len(L)<n:
        return []
    if n==1:
        if s in L:
            return [[s]]
        else:
            return []
    if sum(L[0:n])>s: #L already sorted small to large
        return []
    if sum(L[len(L)-n:-1])+L[-1] < s:
        return []
    #no stop cases hit.
    L2=copy.deepcopy(L)
    hold=L2.pop(0)
    S1 = FindTokens(L2, n-1, s-hold)
    for e in S1:
        e.append(hold)
        e.sort()
    L2=copy.deepcopy(L)
    hold=L2.pop(0)        
    S2 = FindTokens(L2, n, s)
    for e in S2:
        S1.append(copy.deepcopy(e))
    return S1    
        
Nodes=FindTokens([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],4,30)

print("Nodes length ",len(Nodes))

def Overlaps(L1,L2):
    for e in L1:
        for e2 in L2:
            if e==e2:
                return True
    return False         


def findPartners(Nodes):
    L=[]
    n=len(Nodes)
    for i in range(n-1):
        for j in range(i,n):
            if not Overlaps(Nodes[i], Nodes[j]):
                L.append([Nodes[i], Nodes[j]])
    return L            


k=findPartners(Nodes)  #k = collection
print("collection length ", len(k))

def Collides(k1,k2):
    s=set()
    for e in k1[0]:
        s.add(e)
    for e in k1[1]:
        s.add(e)        
    for e in k2[0]:
        s.add(e)
    for e in k2[1]:
        s.add(e)        
    if len(s)==len(k1[0])+len(k1[1])+len(k2[0])+len(k2[1]):
        return False
    else:
        return True


def findBuddies(k):
    G=[]
    n=len(k)
    for i in range(len(k)-1):
        for j in range(i,len(k)):
            if not Collides(k[i],k[j]):
                G.append([k[i],k[j]])
    return G            


G = findBuddies(k) #we have len(Nodes)=86, len(k)=1075, len(G) = 1176

print("Grand set length: ",len(G))

def permute(L,n):
    #Permute list L of length 4
    #according to permutation n=0 to 23
    a,b,c,d = L
    if n==0:
        return [a,b,c,d]
    if n==1:
        return [a,b,d,c]
    if n==2:
        return [a,c,b,d]
    if n==3:
        return [a,c,d,b]
    if n==4:
        return [a,d,b,c]
    if n==5:
        return [a,d,c,b]
    if n==6:
        return [b,a,c,d]
    if n==7:
        return [b,a,d,c]
    if n==8:
        return [b,c,a,d]
    if n==9:
        return [b,c,d,a]
    if n==10:
        return [b,d,a,c]
    if n==11:
        return [b,d,c,a]
    if n==12:
        return [c,a,b,d]
    if n==13:
        return [c,a,d,b]
    if n==14:
        return [c,b,a,d]
    if n==15:
        return [c,b,d,a]
    if n==16:
        return [c,d,a,b]
    if n==17:
        return [c,d,b,a]
    if n==18:
        return [d,a,b,c]
    if n==19:
        return [d,a,c,b]
    if n==20:
        return [d,b,a,c]
    if n==21:
        return [d,b,c,a]
    if n==22:
        return [d,c,a,b]
    if n==23:
        return [d,c,b,a]



def hasColumnMagic(L0,L1,L2,L3):
    a,b,c,d=L0
    p,q,r,s=L1
    u,v,w,x=L2
    m,n,t,z=L3
    if a+p+u+m==b+q+v+n==c+r+w+t==d+s+x+z:
        return True
    return False

def hasDiagonalMagic(L):
    a,b,c,d=L[0]
    p,q,r,s=L[1]
    u,v,w,x=L[2]
    m,n,t,z=L[3]
    if a+q+w+z==d+r+v+m==30:
        return True
    return False

def testCandidate(Gn):
    preMagic=[]
    [a,b],[c,d]=Gn
    for i in range(24):
        for j in range(24):
            for k in range(24):
                if hasColumnMagic(a,permute(b,i),permute(c,j),permute(d,k)):
                    preMagic.append([a,permute(b,i),permute(c,j),permute(d,k)])
    return preMagic                


def findAllPremagic(G):
    allPreMagic=[]
    for i in range(len(G)):
        hold=testCandidate(G[i])
        for e in hold:
            allPreMagic.append(e)
    return allPreMagic        

        
allPreMagic = findAllPremagic(G)

#running a bit... maybe a minute? 2862 premagic squares!
#This is on a torus, so really it's 2862*24*24 = 1,648,512
#for all possible premagic squares...
#to be clear I"m saying 'premagic' to mean both rows and columns sum to 30.



def SquareShift(PM, i, j):
    a=permute(PM[0],i)
    b=permute(PM[1],i)
    c=permute(PM[2],i)
    d=permute(PM[3],i)
    SS=permute([a,b,c,d],j)
    return SS



#Now what remains is to test like this:
# hasDiagonalMagic(SquareShift(allPreMagic[5], 12,10))
# 5 is really 0..2861, other indices are 0..23

print("Ok, trying the last bit now!")


MagicSquares=[]

for num in range(len(allPreMagic)):
    #print(num, end=" ")
    for i in range(24):
        for j in range(24):
            if hasDiagonalMagic(SquareShift(allPreMagic[num],i,j)):
                MagicSquares.append(SquareShift(allPreMagic[num],i,j))  #deep?


print("Done finding All 4x4 Magic Squares")      


#21,120 of these worked!  MagicSquares with diagonals! 
#Surely this is divisible by 8, so      2640*8 of them.


PrimaryMagicSquares=[]


for i in range(len(MagicSquares)):
    if min(MagicSquares[i][0][0],MagicSquares[i][0][3], MagicSquares[i][3][0], MagicSquares[i][3][3])==MagicSquares[i][0][0]:
        if min(MagicSquares[i][0][3], MagicSquares[i][3][0])==MagicSquares[i][0][3]:
            PrimaryMagicSquares.append(copy.deepcopy(MagicSquares[i]))


#RECHECK HERE DOWN!    
#Ok, that's our 2640, not 880.  It doesn't take long to run.
#I seem to have 3x as many as other authors claim exist.  I'm probably
#re-creating them 3x.  Let's see about that...

print("Weeding now...")

for i in range(2639, 0, -1): #No need to get to zero
    if PrimaryMagicSquares.count(PrimaryMagicSquares[i]) > 1:
        PrimaryMagicSquares.pop(i)

for i in range(len(MagicSquares)-1, 0, -1): #No need to get to zero
    if MagicSquares.count(MagicSquares[i]) > 1:
        MagicSquares.pop(i)        


        
import os
fyle=open("magicsquares.txt","w")
for i in range(len(MagicSquares)):
   fyle.write(str(MagicSquares[i])+";\n")
fyle.close()

#in our application, the flipping and rotating matters!




#But now I want all the magic possible...  Put it on a torus...




     
