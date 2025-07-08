'''FOR LOOP EXAMPLES*********************************************************************************************************************************************
name="sravani"
for ch in name:
  print(f"ch={ch}") 
  'fetching names.........................................................._1'
list=["srav","hema","vish"]
for i in list:
  print(i)
  print(f"i={i}")
books={1:"hindi",2:"eng",3:"tel",4:"san",5:"phy"}
for i in books.keys():
    print(f"{i}={books[i]}")
    print(f"{i}={books[i].capitalize()}")'capitalize first letter
n = int(input("Enter the number: "))
for i in range(n):
    print(i * 2)
'even.............................................................._2'
for i in range(2,21,2):
    print(i)
'reverse of even....................................................._3'
for i in range(20,1,-2):
    print(i)
'Multiplication............................................................_4'
for i in range(1,21):
 print(f"15*{i}={15*i}")'''
'WHILE LOOP EXAMPLES************************************************************************************************************************************************'
'Example1:'
email,pwd='vis@gmail.com','vish@123'
max_attempts=5
cur_attempts=1
while cur_attempts<=max_attempts:
  e=input("Enter the email")
  p=input("Enter the password")
  if e==email and p==pwd:
    print("Login successfull!")
    break
  else:
     print("Invalid attempt......try again!")
     cur_attempts=cur_attempts+1
else:
  print("Max attempts are done..try again")
  
