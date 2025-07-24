'''default variabale
def display(name,email,pwd,status='absent'):
    print(name,email,pwd,status)
display(name="srava",email="srav@gmail.com",pwd="12345",status='present')
------------------------------------------------------------------------------
when we donot know bariable length
def display(*var):
    print(var)
display("srava","srav@gmail.com","12345",'present')
display("srava","srav@gmail.com")
display("present")

def SumOfNumbers(n):
 sum=0
 for i in range (1,n+1):
  sum =sum+i
 return sum
n=int(input("Enter a number:"))
print(f"{n}={SumOfNumbers(n)}")'''
def shoot(n):
  if shoot==1:
    return 1
  shoot(n-1)
  print("After recursion",n)
n=int(input("enter the number"))
shoot(n)
 
