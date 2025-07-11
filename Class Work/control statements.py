'''if and else stalement.........................................................................................Example1'
data={'hema@gmail.com':'123@','vishnu@gmail.com':'567&','srav@gmail.com':'789#'}
email,pwd=input("Enter the email and pwd:").split()
if data.get(email)==pwd:
  print("Login successfull")
else:
  print("Invalid credantials")
'Example2...................................................................................................................'
items=['samosa','french fries','ice cream','idly']
stocks=[20,10,50,0]
data=input("Enter the items:")
if data in items:
  ind=items.index(data)
  if stocks[ind]>0:
    print("ava")
  else:
    print("please try again:out of stock")
else:
  print("Item not availaable")
'Exapmle3.......................................................................................................................'

n=int(input("enter the number:"))
if n%2==0 and n%3==0:
  print("divisible by 2 and 3")
elif n%2==0:
 print("only 2")
elif n%3==0:
  print("only 3")
else:
  print("not divisible by 2 and 3")
'Example4...........................................................................................................................'
a=int(input("Enter the a"))
b=int(input("Enter the b"))
if a>b:
  print(f"{a} is greater than {b}")
else:
   print(f"{b} is greater than {a}")
'Example ends...........................................................................................................................'''
