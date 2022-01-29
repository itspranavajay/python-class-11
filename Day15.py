
n = int(input('Enter the number of integers in the numbers : '))
print('Enter ',n,' integers')
nums = [int(input()) for _ in range(n)]
for i in range(0,n,2):
    temp = nums[i+1]
    nums[i+1] = nums[i]
    nums[i] = temp

print(nums)
