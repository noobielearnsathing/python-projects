# #forget about time complexity... :P
# ls=[12,3,1,2,-6,5,-8,6]
# ans=0
# lsc=len(ls)
# i=0
# while(i<lsc):
#     j=i+1
#     while(j<lsc):
#         k=j+1
#         while(k<lsc):
#             if ls[i]+ls[j]+ls[k]==ans:
#                 print(ls[i],ls[j],ls[k],'yes')
#                 exit(0)
#             k+=1
#         j+=1
#     i+=1

# print('no')


#O(n^2) got some hints while he was iterating.. Done most but small error

# ls=[12,3,1,2,-6,5,-8,6]
# ans=0
# ls=sorted(ls)
# # print(ls)

# k=0
# dict1={}
# while(k<len(ls)):
#     i=0
#     j=len(ls)-1
#     while(i<j):
#         if i == k:
#             i+=1
            
#         if j == k:
#             j-=1
            
#         if ls[i]+ls[j]+ls[k] == ans:
#             u=tuple(sorted([ls[i],ls[j],ls[k]]))
#             if u not in dict1:
#                 dict1[u]=True
#                 ##we can use list and make it simple #Actually later I got to know thought it looks simple but weird time complexity is more .. :( There could be some tweaks internally for python to solve the issue I guess..
#             # if m == 0:
#             #     i+=1
#             #     m=1
              
#             # else:
#             #     j-=1
#             #     m=0
#             i+=1
#             j-=1  
            

#         elif ls[i] + ls[j] +ls[k]< ans:
#             i+=1
#         elif ls[i] + ls[j] +ls[k] > ans:
#             j-=1
#     k+=1

# print([i for i in dict1.keys()])






#Yay I solved it.


ls=[12,3,1,2,-6,5,-8,6]
ans=0
ls=sorted(ls)
print(ls)
k=0
ts=[]
i=0
td={}
while(i<len(ls)-1):#he said
    j=i+1
    td={}
    while(j<len(ls)): #due to this it goes out and doesn't affect much i guess
        k=ans-ls[i]-ls[j]
        if k not in td:
            #Here what to assign was confusing and was assigning k but after iterating got to know it should be this. Other some unique way may also be possible If not also worked but last thing will be both same. If in range then outer index bla bla..
            td[ls[j]]=True
        else:
            print(ls[i],ls[j],k)
        j+=1
    # print(td.keys())
    i+=1
   

        
        