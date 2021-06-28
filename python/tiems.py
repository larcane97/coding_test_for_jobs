def check(num:int):
  while num>1:
    if (num%10)==3:
      return True
    else :
      num= int(num/10)
  return False


n = int(input())
ret =0
for i in range(0,n+1):
  for j in range(0,60):
    for k in range(0,60):
      if check(i) or check(j) or check(k):
        ret +=1
print(ret)
