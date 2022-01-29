
n = int(input('Enter the number of elements in the lists : '))

print('Enter ',n,' integers')
L = [int(input()) for _ in range(n)]
print('Enter ',n,' integers')
M = [int(input()) for _ in range(n)]
sum = [L[i]+M[i] for i in range(n)]
print('New list is : ')
print(sum)
