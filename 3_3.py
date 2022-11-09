num=[1,2,3,4,2,4,6,5,2,1,1]
dict={}
for n in num:
    if n in dict:
        dict[n]=dict[n]+1
    else:
        dict[n]=1
print(dict)