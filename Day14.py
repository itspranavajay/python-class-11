
n = int(input('Enter the number of integers in the numbers : '))
print('Enter ',n,' integers')
nums = [int(input()) for _ in range(n)]
nums.reverse()

print(nums)
