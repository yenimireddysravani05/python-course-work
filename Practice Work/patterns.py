'''size = 7 
for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print('*' * size)
    elif i < size // 2:
        print('*')
    else:
        print(' ' * (size - 1) + '*')
for i in range(7):
    if i == 0 or i == 3 or i == 6:
        print("*******")
    elif i < 3:
        print("*")
    else:
       print("       *")
n=7
for i in range(n):
    if i == 0 or i == 3 or i == 6:
        print("*******")
    if i == 1 or i == 2:
        print("*")
    if i == 4 or i == 5:
        print("      *")
n=5
for i in range(n):
    for j in range(n):
        if j==0 :
            print("*",end="")
    print() '''
for i in range(5) :
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end="")
    print()