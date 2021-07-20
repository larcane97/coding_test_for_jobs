
def sort_key(x):
    if x.isdigit():
        return 999
    else:
        return ord(x)

def main():
    s = list(input())
    s.sort(key=sort_key)
    last_num=0
    while s:
        if s[-1].isdigit():
            last_num +=int(s[-1])
            s.pop()
        else:
            break 
    s.append(str(last_num))
    print("".join(s))


if __name__=="__main__":
    main()