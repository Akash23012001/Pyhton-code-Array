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
m=[]
l=0
mAx=[]
for i in range(n):
    s=spin[i]
    for j in s:
        mAx.append(int(j))
    mAx.sort()
    mAx.pop()
    l=max(mAx)
    m.append(l)
    mAx.clear()
Large.append(max(m))
print(Large)
m1=[]
La=0
MAx=[]
for i in range(n):
    s1=spin[i]
    for j in s1:
        MAx.append(int(j))
    La=min(MAx)
    m1.append(La)
    MAx.clear()
Large.append(max(m1))
print(Large)
sum=0
for i in Large:
    sum+=i
print(sum)

    