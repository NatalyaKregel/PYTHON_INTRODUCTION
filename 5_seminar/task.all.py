# Сложение
 
def polyAdd(p1,p2):
    n1=len(p1)
    n2=len(p2)
    if n1>n2:
        n=n1
    else:
        n=n2
    r=[0 for i in range(n)]
    for i in range(n1):
        r[i]+=p1[i]
    for i in range(n2):
        r[i]+=p2[i]
    for i in range(n):
        j=n-i-1
        print(j)
        if r[j] !=0:
            break
        else:
           del r[j]
    return r
 
# Вычитание
 
def polySub(p1,p2):
    p3=[-a for a in p2]
    return polyAdd(p1,p3)
    
# Умножение 
 
def polyMult(p1,p2):
    n1=len(p1)
    n2=len(p2)
    n=n1+n2-1
    r=[0 for i in range(n)]
    for k in range(n):
        for i in range(k+1):
            j=k-i
            if (j<n2) and (i<n1):
                r[k]+=p1[i]*p2[j]
    return r
   
# Нормальная печать
 
def polyPrint(p):
    flgf=0
    res=""
    for i in range(len(p)):
        a=p[i]
        if a==0:
            continue
        if abs(a)==1:
            if a>0:
                if flgf==0:
                    z="1"
                else:
                    z="+"
            else:
                z="-"
        else:
            if flgf==0:
                z=str(a)
            else:
                if (a>0):
                    z="+"+str(a)
                else:
                    z=str(a)
        if (i>=1):
            z+="x"
        if (i>=2):
            z+="^"+str(i)
        res+=z
        flgf=1
    return res
 
# Парсинг
 
def parsePoly(p):
    r=[]
    acc=""
    for a in p:
        if a=="-" or a=="+":
            if acc != "":
                r+=[acc]
            acc=a
        else:
            acc=acc+a
    r+=[acc]
    return r
    
# Ввод полинома в естественном виде
 
def inputPoly(p):
    tmp=parsePoly(p)
    d=0
    if p.find("x") >= 0:
        d=1
    for mon in tmp:
        k=mon.find("^")
        if k>=0:
            z=int(mon[k+1:])
            if z>d:
                d=z
    r=[0 for i in range(d+1)]
    for mon in tmp:
        k=mon.find("x")
        u=mon.find("^")
        if k==-1 and u==-1:
            r[0]=r[0]+int(mon)
            continue
        if mon=="x":
            mon="+1x"
        elif mon[2]=="-x":
            mon="-1"+mon[1]
        elif mon[2]=="+x":
            mon="+1"+mon[1]
        elif mon[0]=="x":
            mon="+1"+mon
        if u==-1:
            mon=mon+"^1"
        k=mon.find("x")
        u=mon.find("^")
        c=int(mon[:k])
        z=int(mon[u+1:])
        r[z]=r[z]+c
    return r
    
# Тесты
 
s1=inputPoly("x+1")
s2=inputPoly("x^2+2x+1")
s3=polyMult(s1,s2)
print(polyPrint(s3))
 
 
print(inputPoly("-3+7x^3-5x^2+8"))
print(inputPoly("x"))
 
s2=inputPoly("x^2+1")
print(s2)    
 
s1=inputPoly("x-1")
s2=inputPoly("1")
for i in range(100):
    s2=polyMult(s1,s2)
print(polyPrint(s2))
2