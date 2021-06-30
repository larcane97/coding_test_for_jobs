
## Selection Sort
def selection_sort():
    arr=[7,5,9,0,3,1,6,2,4,8]
    for i in range(len(arr)):
        idx=i
        for j in range(i+1,len(arr)):
            if arr[idx] > arr[j]:
                idx=j
        arr[idx],arr[i] = arr[i],arr[idx]
    print(arr)
selection_sort()

def insert_sort():
    arr=[7,5,9,0,3,1,6,2,4,8]
    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    print(arr)
print()
insert_sort()


arr=[7,5,9,0,3,1,6,2,4,8]
def quick_sort(start,end):
    if end <= start :
        return
    pivot = end
    left,right=start-1,start-1
    for i in range(start,end):
        if arr[i] >= arr[pivot]:
            right+=1
        else:
            arr[left+1],arr[i] = arr[i],arr[left+1]
            left+=1
            right+=1
    arr[left+1],arr[pivot] = arr[pivot],arr[left+1]
    quick_sort(start,left)
    quick_sort(left+2,end)
quick_sort(0,len(arr)-1)
print()
print(arr)


arr=[7,5,9,0,3,1,6,2,4,8]
def quick_sort2(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x<=pivot]
    right =[x for x in tail if x>pivot]

    return quick_sort2(left)+[pivot]+quick_sort2(right)
print()
print(quick_sort2(arr))











