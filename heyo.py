

n=int(input())
x=[]
d=[]
for i in range(n):
 a,b,c=input().split()
 d.append(c)
 l=[]
 
 for i in range(int(a)):
  
  stack=input().split()
  
  for h in range(len(stack)):
     stack[h]=int(stack[h]) 
  l.append(stack)
  s=[]
  for g in range(len(l)):
      for k in range(len(l[g])):
          s.append(l[g][k])
   
 s.sort(reverse=True)
 x.append(s)
 print(x)








for a in range(len(d)):
    d[a]=int(d[a])
print(x,d)
for i in range(len(x)):
  count=i+1
  sum=0
  for j in range(d[i]):
      sum=sum+x[i][j]
  print('Case #%d: %d'%(count,sum))