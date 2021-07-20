def solution():
    s = input()
    ret= 10000
    # 묶음 단위 : 1~s의 길이
    for i in range(1,len(s)+1):
        tmp=''
        dup_num=1
        for cur in range(0+i,len(s)+1,i):
            if s[cur-i:cur]==s[cur:cur+i]:
                dup_num+=1
            else:
                if dup_num==1:
                    tmp +=s[cur-i:cur]
                else:
                    tmp +=str(dup_num)+s[cur-i:cur]
                    dup_num=1
        tmp +=s[cur:]
        if ret > len(tmp):
            ret = len(tmp)
    return ret

if __name__=="__main__":
    solution()