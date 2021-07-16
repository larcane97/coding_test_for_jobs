numbers=input()
numbers = [int(i) for i in numbers]

ret=numbers[0]
for i in range(1,len(numbers)):
    ret = max(ret+numbers[i],ret*numbers[i])
print(ret)