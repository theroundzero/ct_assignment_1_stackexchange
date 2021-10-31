from operator import itemgetter
import sys

prevword = None
counter = 1 
words = None
df={}
dl=[]
# input comes from STDIN
for word in sys.stdin:
    w,z= word.strip().split('\t', 1)
    dat,nNc = z.split(' ',1)
    n,Nc=nNc.split(' ',1)
    N,c=Nc.split(' ',1)
    if prevword == w:
        counter = counter+int(c)
    else:
        if prevword != None:
            q=n+' '+N+' '+str(counter)
            df[prevword]=q
            j=prevword+' '+dat
            dl.append(j)
        counter=1
        prevword = w

       
q=n+' '+N+' '+str(counter)
df[prevword]=q
j=prevword+' '+dat
dl.append(j)

for h in l1:
   w,dat=h.split(' ',1)
   for d in df:
       if w == d:
          print '%s\t%s' % (h,df[d])
    
