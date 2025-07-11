'Arithmetic Operators.........................'
a=10
b=20
print("addition:",a+b)#addition: 30
print("sub:",a-b)#sub: -10
print("mul:",a%b)#mul: 10
print("floor div:",a//b)#floor div: 0
print("power:",a**b)#power: 100000000000000000000
print("mul:",a*b)#mul: 200
' Comparison opeartors.py.....................................................'
print(a==b)#False
print(a>=b)#False
print(a<=b)#True
print(a>b)#False
print(a<b)#True
print(a!=b)#True
'Assignment operator.........................................................'
a=a+b
print(a)#30
a=a-b
print(a)#10
a=a*b
print(a)#200
a=a/b
print(a)#10.0
a=a//b
print(a)#0.0
a=a+7
print(a)#7.0
a=a**3
print(a)#343.0
b=b%a
print(b)#20.0
a=a+10
print(a)#353.0
e=7
e=e-1
print(e)#6
'logical opeartor............................................................'
x=10
y=5
print(x>5 and y<x)#True
print(x>y or y>x)#True
print(not(x>y))#False
'Membership operator...........................................................'
names=["sraavni","hema","vishnu"]
print("hema" in names)#True
print("vishnu" not in names)#False
print("surya" in names)#False
'Identity operator..............................................................'
l=[1,2,3,4]
m=l
n=[1,2,3,4]
print(l is m)#True
print(l is not m)#False
print(l is n)#False
print(id(l))#2364723471744
print(id(n))#2364725233024
'Bitwise Operator...................................................................'
a=5
b=6
print(a&b)#4
print(a|b)#7
print(a^b)#3
print(~a)#-6
print(a<<b)#320
print(a>>b)#0