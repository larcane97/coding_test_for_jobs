numbers = list(input())
left = numbers[0:len(numbers)//2]
right = numbers[len(numbers)//2:]
left_sum,right_sum=0,0
for i in left:
    left_sum+=int(i)
for i in right:
    right_sum+=int(i)

if left_sum==right_sum:
    print("LUCKY")
else:
    print("READY")
