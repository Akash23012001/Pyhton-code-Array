n=4
spin=['812','266','256','244']
Large=[]
M=[]
L=0
Max=[]
for i in range(n):
    S=spin[i]
    for j in S:
        Max.append(int(j))
        # Max.sort()
    L=max(Max)
    M.append(L)
    Max.clear()
    # print(Max)
Large.append(max(M))
M.clear()
L=0
Max.clear()
# m=[]
# mAx=[]
for i in range(n):
    s=spin[i]
    for j in s:
        Max.append(int(j))
    Max.sort()
    Max.pop()
    L=max(Max)
    M.append(L)
    Max.clear()
Large.append(max(M))
print(Large)
# m1=[]
# La=0
# MAx=[]
M.clear()
Max.clear()
L=0
for i in range(n):
    s1=spin[i]
    for j in s1:
        Max.append(int(j))
    L=min(Max)
    M.append(L)
    Max.clear()
Large.append(max(M))
print(Large)
sum=0
for i in Large:
    sum+=i
print(sum)

    