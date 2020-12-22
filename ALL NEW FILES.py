print("hello world")
s=0
for i in range(0,1201):
    s= s+i

print("The sum of the first 1200 interger is :",s)



def max_sum(A):
    N=len(A)
    sums=[sum(A[i:j+1]) for i in range(N) for j in range(i,N)]
    return max(sums)

A = [1,3,4,-8,2,3,-1,3,4,-3,10,-3,2]
print(A)
print(max_sum(A))

i=[1,2,3,5]
for j in range(len(i)):
    print(i[j+1])
    

