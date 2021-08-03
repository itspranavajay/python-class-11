
n = int(input('Enter the number of integers in the numbers : '))
nums = []

print('Enter ',n,' integers')
for i in range(0,n):
    nums.append(int(input()))

for i in range(0,n,2):
    temp = nums[i+1]
    nums[i+1] = nums[i]
    nums[i] = temp

print(nums)
