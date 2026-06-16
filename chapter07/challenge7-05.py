list1=[8,19,148,4]
list2=[9,1,33,83]

ans=[]

#list1から数字を1つずつ取り出してiに入れる
for i in list1:
    #list2から数字を1つずつとりだしてjに入れる
    for j in list2:
        ans.append(i * j)

print(ans)
