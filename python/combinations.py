import sys
#def combinations(iterable, r):
# combinations('ABCD', 2) --> AB AC AD BC BD CD
# combinations(range(4), 3) --> 012 013 023 123
iterable = [0,1,2]
r = 2
pool = tuple(iterable)
n = len(pool)
#if r > n:
    #return
indices = list(range(r))
#yield tuple(pool[i] for i in indices)
print(tuple(pool[i] for i in indices))
print("Hola")
while True:
    for i in reversed(range(r)):
        if indices[i] != i + n - r:
            break
    else:
        sys.exit('Done.')
    indices[i] += 1
    for j in range(i+1, r):
        indices[j] = indices[j-1] + 1

    #yield tuple(pool[i] for i in indices)
    oneIndices = tuple(pool[i] for i in indices)
    print(oneIndices)

    Rs = [1]+[0]*(n**4-1)
    for i in oneIndices:
        Rs[i+1] = 1




#print(list(combinations([0,1,2,3,4,5,6,7],3)))
