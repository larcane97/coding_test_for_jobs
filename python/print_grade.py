n = int(input())
arr=[]
for i in range(n):
    arr.append(tuple(input().split()))
arr.sort(key=lambda a:int(a[1]))
for i in arr:
    print(i[0],end=' ')