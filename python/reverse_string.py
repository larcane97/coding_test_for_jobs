def solve1():
    s = input()
    one = 0
    zero=0
    for text in s.split('0'):
        if text:
            one+=1

    for text in s.split('1'):
        if text:
            zero+=1

    print(min(one,zero))

def solve2():
    s = input()
    one,zero=0,0
    if s[0]=='1':
        zero+=1
    else:
        one+=1
    
    for i in range(1,len(s)):
        if s[i] !=s[i-1]:
            if s[i]=='1':
                zero+=1
            else:
                one+=1
    print(min(zero,one))

if __name__=='__main__':
    solve1()
    solve2()

