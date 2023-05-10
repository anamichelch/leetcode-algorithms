def binary_search(nums, target):
    low = 0
    upper = len(nums) - 1

    while low <= upper:
        mid = (upper + low) // 2

        if target == nums[mid]:
            print(mid)
            return mid
        elif target < nums[mid]:
            upper = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search_recursive(nums, target, args*):
    if left < right:
        return -1
    mid = (left+right)//2

    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search_recursive(nums, target,  left = left, mid-1)
    else:
        return binary_search_recursive(nums, target,mid+1,right )
    pass


nums = [-1, 0, 3, 5, 9, 12]
target = 9
binary_search(nums, target)
binary_search_recursive(nums,target)
