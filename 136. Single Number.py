
def singleNumber(nums):
    dict = {}

    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    for num in dict:
        if dict[num] == 1:
            return num

    return -1


nums = [4,1,2,1,2]
print(singleNumber(nums))