'''n=input("Enter the number:")
sum=0
for i in n:
  sum=sum+int(i)
print(sum)
def sum(n):
  if n==0:
    return 0
  return n%10+sum(n//10)
n=int(input("Enter the number"))  
print(sum(n))'''

n=int(input("Enter the number"))  
a,b=0,1
for i in range(n):
  print(a,end="")
  a,b=b,a+b