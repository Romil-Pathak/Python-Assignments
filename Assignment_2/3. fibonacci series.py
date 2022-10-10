num = int(input("Enter the fibonacci series range: "))
n1 = 0
n2 = 1
for i in range(0, num):
    if i<=1:
        number = i
    else:
        number = n1 + n2
        n1 = n2
        n2 = number
    print(number, end=', ')
print()
'''i=0
while i<num:
    print(n1, end=', ')
    nth = n1+n2
    n1=n2
    n2=nth
    i+=1
print()
'''