##working but kth element is same as index number
import random
def par(lis,l, r, p):
    # print(lis[p])
    pe = lis[p]
    # print(lis)
    lis[p],lis[r]= lis[r], lis[p]
    si = l
    for i in range(l,r):
        if lis[i] < pe:
            lis[si],lis[i] = lis[i],lis[si]
            si += 1
    lis[si],lis[r] = lis[r],lis[si]
    # print(lis,'par')
    return si
#[3,45,67,25,437,89,6,0]
def select(li,l,r,k):
    while True:
        if l == r:
            return li[r]
        pi = random.randint(l,r)
        # pi = l+r // 2
        pi = par(li, l, r, pi)
        if k == pi:
            return li[k]
        elif k < pi:
            r = pi-1
        else:
            l = pi+1
        # print(li,'sel')

a = [3,45,67,25,437,89,6,0]
# a = [1,2,3]
print(select(a,0,len(a)-1,5))
print(a)
print(sorted(a))

