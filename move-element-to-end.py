# ls=[2,1,2,2,2,3,4,2]
# ls=[1,3,4,2,2,2,2,2]
# ele=2
# i=0
# c=0
# while(c<len(ls)):
#     if ls[i] == ele:
#         del ls[i]
#         ls.append(ele)
#     else:
#         i+=1
#     c+=1
# print(ls)

#prog 2
ls=[2,1,2,2,2,3,4,2]
i,j=0,len(ls)-1
while(i<j):
    if ls[i] == 2 and ls[j]!=2:
        ls[i],ls[j]=ls[j],ls[i]
    if ls[i] !=2:
        i+=1
    if ls[j]==2:
        j-=1
print(ls)