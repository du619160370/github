nums = [3, 4, 3, 5]
target = 6
n = 0
flag = 0
while n < len(nums):
    a = nums.pop(n)
    b = target - a
    if b in nums:
        for i in range(0, len(nums)):
            if b == nums[i]:
                a = n
                b = i + 1
                flag = 1
                break
        break
    else:
        nums.insert(n, a)
        n += 1
if flag:
    result = list()
    result.append(a)
    result.append(b)
    print(result)
else:
    print("No result.")


