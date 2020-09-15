#Worked but huge runtime
# ls=[3,5,-4,8,11,1,-1,6]
# ans=5
# f=0
# for i,a in enumerate(ls):
#     j=i+1
#     while(j<len(ls)):
#         if a+ls[j] == ans:
#             print(a,ls[j],'yes')
#             f=1
#             break

#         j+=1
#         # print(i,j)
#     if f==1:
#         break
    

#Not worked because should consider both ways like not just right side half
# ls=[3,5,-4,8,11,1,-1,6]
# ans=10
# low=0
# high=len(ls)-1
# ls=sorted(ls)
# print(ls)
# if ls[low]+ls[high] == ans:
#     print('yes')
#     exit(0)
# print(ls[low],ls[high])
# while(low<=high):
#     k=ls[low]+ls[high]
#     mid = (high+low)//2
#     if ans > ls[mid]+ls[high]:
#         low=mid+1
#     elif ans < ls[mid]+ls[high]:
#         high=mid-1
#     else:
#         print('yes')
#         break
#     print(ls[low],ls[high])

#This is a good algo I guess..
# ls=[3,5,-4,8,11,1,-1,6]
# ans=8
# ls=sorted(ls)
# print(ls)
# i=0
# j=len(ls)-1

# while(i<j):
#     if ls[i]+ls[j] == ans:
#         print('yes')
#         break
#     elif ls[i] + ls[j] < ans:
#         i+=1
#     elif ls[i] + ls[j] > ans:
#         j-=1
#     print(ls[i],ls[j])

# ls=[3,5,-4,8,11,1,-1,6]
# ans=10
# d={}
# f=0
# for i in ls:
#     if i not in d: #if ans-i not in d:
#         d[ans-i]=True #d[i]=True
#     else:
#         print('yes')
#         f=1
#         break

# if f == 0:
#     print('no')
