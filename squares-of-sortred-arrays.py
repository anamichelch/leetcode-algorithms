def sorting_squared_arr(arr):
    return print(sorted(arr[i]**2 for i in range(len(arr))))



nums = [-4,-1,0,3,10]
Output= [0,1,9,16,100]
sorting_squared_arr(nums)
