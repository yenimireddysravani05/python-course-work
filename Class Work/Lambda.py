'''def squares(n):
    return n * n
n = int(input("enter the number"))
print(squares(n))

def squares(l):
  for i in range(len(l)):
     l[i]=l[i]**2
  return l
l=[1,2,3,4,5]
print(squares(l))

n=[1,2,3,4,5]
sua=list(map(lambda i:i+10,n))
print(sua)

s='python'
vol='aeiou'
m=list(map(lambda i:'*' if i in vol else i,s))
print(m)


from functools import reduce
numbers=['name','name2','name3']
ch=reduce(lambda x,y:x+y,numbers)
print(ch)'''

#list comprehension
l=[]
for i in range(1,11):
   l.append(i)
print(l)

k={i for i in range(1,11)}
print(k)
l=[]

for i in range(1,11):
  if i%2==0:
    l.append(i)
print(l)

k=list([i for i in range(1,11) if i%2==0])
print(k)


