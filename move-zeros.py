def move_zeros(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[count] == 0:

            nums.append(0)

            nums.pop(count)

        else:
            count += 1
            pass
    print(nums)

arr = [0, 1, 0, 3,12]
arr = [0, 1, 0, 3,12]
arr2 = [0, 1, 0, 3,12,0,4,7,0]
move_zeros(arr)
move_zeros(arr2)