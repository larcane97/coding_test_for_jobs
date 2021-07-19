
def search(cur:int,value:int,check:list,values:list):
    check.append(value)
    for idx in range(cur+1,len(values)):
        search(idx,value+values[idx],check,values)


def main():
    n =int(input())
    values = list(map(int,input().split()))
    check=list()
    search(-1,0,check,values)
    check = list(set(check))
    for i in range(1,1000*1000000 +1):
        if not i in check:
            print(i)
            break
    print(check)

def solution():
    n = int(input())
    values = list(map(int,input().split()))
    values.sort()
    target=1
    
    for value in values:
        if target <value:
            break
        target+=value
    print(target)
if __name__=="__main__":
    main()
    solution()


