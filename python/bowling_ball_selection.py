from collections import Counter
import math


def solve1():
    n,m = map(int,input().split())
    weights= map(int,input().split())
    total_num = math.comb(n,2)

    same_weights = Counter(weights)
    for i in range(1,m+1):
        if same_weights[i]>1:
            total_num -=math.comb(same_weights[i],2)
            
    print(total_num)

def solve2():
    n,m=map(int,input().split())
    arr = list(map(int,input().split()))
    num_count=[0]*(m+1)

    for num in arr:
        num_count[num]+=1
    
    result=0
    for i in range(1,m+1):
        cur = num_count[i]
        n -=cur
        result += cur*n
    print(result)


if __name__=="__main__":
    solve1()
    solve2()