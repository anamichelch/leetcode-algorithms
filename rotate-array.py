def rotate_arr(nums,k):
    arr_len = len(nums)
    for i in range(arr_len):
        if i + (k-1) > arr_len-1:
            delta = arr_len - i
            index = -1
            new_index = index + delta + k-1
            temp = nums[i + k - 1]
            nums[i + k - 1] = nums[i]
        temp = nums[i+k-1]
        nums[i+k-1] = nums[i]








nums = [1,2,3,4,5,6,7]
k = 3
