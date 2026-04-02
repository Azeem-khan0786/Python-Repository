def binarySearch(nums,x):
    n=len(nums)
    start,end=0,n-1
    while start<=end:
        mid=(end+start)//2
        if nums[mid]==x:
            return mid
        elif nums[mid]<x:
            start=mid+1
        else:
            end=mid-1
    return -1            
nums= [12,31,34,11]
x=34
target=binarySearch(nums,x)
print(f"Search index of given element{x}",target)
