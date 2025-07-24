#6
'''n=set(input().split(','))
print(sorted(n))
#7
n=int(input())
data={}
max_val=0
res=''
for i in range(n):
  name,mark=input().split()
  mark=int(mark)
  if mark>max_val:
    res=name
  data[name]=mark
print(data)
print(name)'''
#8
n=input().split()
for i in range(len(n)):
  n[i]=n[i][::-1]
print(' '.join())