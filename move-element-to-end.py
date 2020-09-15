ls=[2,1,2,2,2,3,4,2]
ls=[1,3,4,2,2,2,2,2]
ele=2
i=0
c=0
while(c<len(ls)):
    if ls[i] == ele:
        del ls[i]
        ls.append(ele)
    else:
        i+=1
    c+=1
print(ls)
