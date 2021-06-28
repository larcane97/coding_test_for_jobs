def in_range(x:int,y:int,n:int):
  return x>0 and x<=n and y>0 and y<=n

dir=[
  [0,1],
  [1,0],
  [-1,0],
  [0,-1]
]
n = int(input())
direction = list(map(str,input().split()))

x=1
y=1
for d in direction:
  dx=x
  dy=y
  if d=='R':
    dx +=dir[0][0]
    dy +=dir[0][1]
    if in_range(dx,dy,n):
      x=dx
      y=dy
  elif d=='L':
    dx +=dir[3][0]
    dy +=dir[3][1]
    if in_range(dx,dy,n):
      x=dx
      y=dy
  elif d=='U':
    dx +=dir[2][0]
    dy +=dir[2][1]
    if in_range(dx,dy,n):
      x=dx
      y=dy
  elif d=='D':
    dx +=dir[1][0]
    dy +=dir[1][1]
    if in_range(dx,dy,n):
      x=dx
      y=dy

print(x,y)
