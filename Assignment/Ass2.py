'''1
salary=float(input())
if salary<=250000:
    print("No Tax")
elif salary>250000 and salary<=500000:
    print(salary*0.05)
elif salary>500000 and salary<=1000000:
    print(salary*0.2)
elif salary>1000000:
    print(salary*0.3)

'2'    
n=int(input())
total=0
for _ in range(n):
    age=int(input())
    if age>=5 and age<=18:
        total+=100
    elif age>=19 and age<=60:
        total+=150
    elif age>60:
        total+=120
print(total)
    
'3'
units=int(input())
bill=0
if units<=100:
    bill+=units*1.5
units=units-100
elif units>100 and units<=




'4'
hrs=int(input())
fee=0
if hrs<=2:
   print(30)
elif hrs>2 and hrs<24:
   fee=30+(hrs-2)*10
elif hrs>24:
   print(200)


'5'
name=input()
qua=int(input())
if qua==0:
    print("Out of Stock")
elif qua>0 and qua<=10:
    print("Low Stock")
elif qua>11 and qua<=50
    print("Instock")
elif qua>50:
    print("Full stock")
    
    
'6'
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j)%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()

'7'
ch=int(input())
ppl=int(input())
if ch==1:
    print(ppl*500)
elif ch==2:
    print(ppl*1400)
elif ch==3:
    print(ppl*5000)
else:
    print("invalid choice")

'8'
 
total=float(input())
if total<1000:
    print(total)
elif total>999 and total<5000:
    print(total-total*0.05)
elif total>4999 and total<10000:
    print(total-total*0.1)
elif total>=10000:
    print(total-total*0.15)

'9'
pin=1234
for _ in range(3):
    epin=int(input())
    if epin==pin:
        print("Access Granted")
        break
else:
    print("ATM Blocked:TRy Again later!")'''

    
'10'
total_seats=int(input())
booked_seats=list(map(int,input().split()))
print(f"Total seats:{total_seats}")
print(f"Booked seats:{len(booked_seats)}")
print(f"Avilable seats:{total_seats-len(booked_seats)}")
    
                  


