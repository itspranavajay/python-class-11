
n = int(input('Enter the number of elements in the lists : '))

L = []
M = []

print('Enter ',n,' integers')
for i in range(0,n):
    L.append(int(input()))

print('Enter ',n,' integers')
for i in range(0,n):
    M.append(int(input()))

sum = []
for i in range(0,n):
    sum.append(L[i]+M[i])

print('New list is : ')
print(sum)
