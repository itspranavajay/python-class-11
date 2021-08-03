
n = int(input('Enter the number of integers in the numbers : '))
nums = []

print('Enter ',n,' integers')
for i in range(0,n):
    nums.append(int(input()))

nums.insert(0,nums[n-1])
nums.pop()

print(nums)
