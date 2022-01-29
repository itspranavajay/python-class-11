
n = int(input('Enter the number of integers in the numbers : '))
print('Enter ',n,' integers')
nums = [int(input()) for _ in range(n)]
nums.insert(0,nums[n-1])
nums.pop()

print(nums)
