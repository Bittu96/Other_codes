

from collections import Counter
from collections import defaultdict
import testData


# def freqQuery(query, box = Counter(), result=[]):
#     for i,v in query:
#         if i==3: result.append( (0,1) [v in box.values()] )
#         elif i==1: box[v]+=1
#         else:
#             if box[v]>0: box[v]-=1
#     return (result)


def freqQuery( query, box=defaultdict(), freq=defaultdict(), result=[]):
    for i,v in query:
        if i==3:
            try: result.append( (0,1) [freq[v]>0] )
            except: result.append(0)
        else:
            if v in box:
                try: freq[box[v]]-=1
                except: freq[box[v]]=1
                box[v]+=1 if i==1 else -1 if box[v]>0 else 0
            else:
                box[v]=1
            try: freq[box[v]]+=1
            except: freq[box[v]]=1
    return result


# def freqQuery( queries, freq = Counter(), cnt = Counter(), arr = [] ):
#     for q in queries:
#         if q[0]==1:
#             cnt[freq[q[1]]]-=1
#             freq[q[1]]+=1
#             cnt[freq[q[1]]]+=1

#         elif q[0]==2:
#             if freq[q[1]]>0:
#                 cnt[freq[q[1]]]-=1
#                 freq[q[1]]-=1
#                 cnt[freq[q[1]]]+=1
#         else:
#             if cnt[q[1]]>0:
#                 arr.append(1)
#             else:
#                 arr.append(0)
#     return arr



arr = testData.data1
arr = list(map(int,arr.split()))
print(len(arr))
ar = [[arr[2*i],arr[2*i +1]] for i in range(100000)]
print(len(ar))

que = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]


#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
import time
start_time = time.time()
#LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL

ans = freqQuery(ar)

#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
print("--- %ls seconds ---" % (time.time() - start_time))
#LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL


# print(ans)
testans = list(map(int,testData.data1ans.split()))
print(Counter(ans),Counter(testans))

