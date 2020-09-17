# a=[-1,5,10,20,28,3]
# b=[26,134,135,15,17]
# a.sort()
# b.sort()
# i=0
# j=0
# ds={}
##sorting
# while(i<len(a) and j<len(b)):
#     if a[i]<b[j]:
#         ds[a[i]]=1
#         del a[i]
#     elif b[j]<a[i]:
#         ds[b[j]]=0
#         del b[j]
#     else:
#         ds[a[i]]=1
#         ds[b[j]]=0
#         del a[i]
#         del b[j]



# while i<len(a):
#     ds[a[i]]=1
#     i+=1

# while j<len(b):
#     ds[b[j]]=0
#     j+=1

# # maxi = float('inf')#mini variable is good..
# ls=list(ds)
# diff=float('inf')

# for i in range(len(ls)-1):
#     if ds[ls[i+1]] != ds[ls[i]]:
#         diff = abs(ls[i+1]-ls[i])
#     else:
#         pass
#     if diff < maxi:
#         maxi=diff
#         maxi1=(ls[i],ls[i+1])

# print(maxi1)
# # maxi=float('inf')
# # for i in range(len(ls)-1):
# #     if ds[i+1]-ds[i]<maxi:
# #         maxi=abs(ls[i+1]-ls[i])
# #         maxi1=(ls[i],ls[i+1])
# # print(maxi1)


a=[-1,5,10,20,28,3]
b=[26,134,135,15,17]
# [-1, 3, 5, 10, 20, 28]
# [15, 17, 26, 134, 135]
a.sort()
b.sort()
# print(a)
# print(b)
i=0
j=0
mini=float('inf')
minil=[]
while(i<len(a) and j<len(b)):
    # if (a[i] < b[j]):
    #     if mini>(b[j]-a[i]):
    #         mini=a[i]+b[j]
    #         minil=[a[i],b[j]]
    #     i+=1
    # elif (a[i]>b[j]):
    #     if mini>(-b[j]+a[i]):
    #         mini=(a[i]-b[j])
    #         minil=[a[i],b[j]]
    #     j+=1
    
    if (a[i] != b[j]):
        if mini>abs(a[i]-b[j]):
            mini=abs(a[i]-b[j])
            minil=[a[i],b[j]]
        if a[i]>b[j]:
            j+=1
        else:
            i+=1
    else:
        mini=abs(a[i]-b[j])
        minil=[a[i],b[j]]

print(mini)
print(minil)