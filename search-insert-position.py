def search_insert(nums,target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = left + (right-left)//2
        if target == nums[mid]:
            return print(mid)
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return print(left)

nums = [2,3,5,6]
target = 5
search_insert(nums,target)
search_insert(nums,7)
search_insert(nums,0)