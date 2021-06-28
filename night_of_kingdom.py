import sys

def in_range(x:int,y:int):
  return 0<x<=8 and 0<y<=8

def int2str(x:int):
  return chr(x+ord('a')-1)
def str2int(x:str):
  return int(ord(x)-ord('a'))+1

dir = [
  [0,1],
  [1,0],
  [-1,0],
  [0,-1]]
loc = sys.stdin.readline().rstrip()
x = int(loc[1])
y = str2int(loc[0])
ret=0
for i in range(4):
  dx = x+ dir[i][0]*2
  dy = y+ dir[i][1]*2
  if x==dx:
    if in_range(dx+1,dy):
      ret+=1
    if in_range(dx-1,dy):
      ret+=1
  elif y==dy:
    if in_range(dx,dy+1):
      ret+=1
    if in_range(dx,dy-1):
      ret+=1
print(ret)