x = 'Hello python'
dict = {}
for i in x:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

