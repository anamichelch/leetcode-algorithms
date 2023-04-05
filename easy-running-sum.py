def running_sum(nums):
    index_to_sum = 0
    lenght = len(nums)
    new_list = [nums[0]]
    for i in range(1, lenght):
        sum = nums[index_to_sum] + nums[i]
        nums[i] = sum
        new_list.append(sum)
        index_to_sum += 1
    return new_list

print(running_sum([1,2,3,4]))
print(running_sum([1,1,1,1,1]))
print(running_sum([3,1,2,10,1]))