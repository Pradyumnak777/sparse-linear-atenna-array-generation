def diffChecker(lst):
    result = [0]*(lst[-1]+1)
    dontCount = set() 
    result[0] =  n
    result[-1] = 1
    for i in range(1,lst[-1]):#diff_Values
        dontCount = set()
        for j in lst: #list value 
            if j == None:
                continue
            if((j + i) in lst and frozenset((j,j+i)) not in dontCount):
                result[i] += 1
                dontCount.add(frozenset((j,j+i)))
            elif((j-i) in lst and frozenset((j,j-i)) not in dontCount):
                result[i] += 1
                dontCount.add(frozenset((j,j-i)))
    return result


def arrayGen(n,proto,choiceList,avail,k):
        global N
        proto[-1] = N
        if None not in proto:
            lst = diffChecker(proto)
            if 0 in lst[1:len(lst)-1]: #now we backtrack
                # print(f"{proto} is not a solution\n")
                return
            else:
                #break, take it outside of the function and pass it back in after initialization
                print(f"{proto} is a solution, so now we check for higher N\n")
                N+=1
                proto = [None]*n
                proto[-1] = N
                proto[0] = 0
                avail = [1]*(N-1)
                choiceList = []
                for i in range(1,N):
                    choiceList.append(i)
                arrayGen(n,proto,choiceList,avail,N)
                
        k = N
        for i in range(1,n):
            if proto[i] is None: 
                for j in range(0,N) :
                    if j >= k-1:
                        return
                    if avail[j] == 1:
                        proto[i] = choiceList[j]
                        avail[j] = 0
                        arrayGen(n,proto,choiceList,avail,k)
                        if(N > k):
                            return
                        proto[i] = None
                        avail[j] = 1
        



#driver/main code-
global n
n = int(input("Enter array size: "))
N = n # dynamic upper limit, aperture size
proto = [None]*n #length of resultant array is fixed
proto[0] = 0 #first element is always 0
proto[-1] = N

choiceList = []
available = [1]*(N-1)
for i in range(1,N):
    choiceList.append(i)

arrayGen(n, proto, choiceList, available,N)
print("max N is : ",N-1)
