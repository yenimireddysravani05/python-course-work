'''l=[10,20,30]
for i in range(10):
    new_l=int(input())
    l.append(new_l)
print(l)
#2 to 100 even numbers
#2 to 100 prime numbers
#palindrame
for i in range(2,100,2):
        print(i,end=" ")
   
for i in range(2,100):
   for j in range(2,i):
       if i%j==0:
           break
   else:
       print(i)
         
n=141
temp=n
rev=0
while temp>0:
    ld=temp%10
    rev=rev*10+ld
    temp=temp//10
    
if n==rev:
    print("palindroome")
else:
    print("Not palindrome")
    
n="mam"
if n==n[::-1]:
    print("palin")
else:
    print("not palin")'''


name="subb"
rev=""
for ch in range(len(name)-1,-1,-1):
    rev=rev+name[ch]
if name==rev:
 print("pal")
else:
 print("not pal")

