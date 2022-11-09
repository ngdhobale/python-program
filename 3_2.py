list1 = [3, 6, 9, 12, 15, 18, 21,78,34]
for i in range(0,len(list1),4):
    l=list1[i:i+4]
    print(list(reversed(l)))
