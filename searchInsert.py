import math
nums = [1,3,5,6]


def search(nums,l,h,target):
    if l==h:
        if nums[l]==target:
            return l
        else:
            return 0
    else:
        mid = math.ceil((l+h)/2)
        if nums[mid] == target:
            return mid
        if nums[mid]>target:
            l=0
            h=mid-1
            return search(nums,l,h,target)
        if nums[mid]<target:
            l=mid+1
            h=len(nums)
            return search(nums,l,h,target)


l=0
h=len(nums)
#print(l,h)
target = 2
print(search(nums,l,h,target))