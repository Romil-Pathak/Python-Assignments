x = input("Enter a string:")
if len(x)>=3:
    if x[-3:]== 'ing':
        x = x + 'ly'
        print(x)
    else:
        x = x + 'ing'
        print(x)
else:
    print(x)