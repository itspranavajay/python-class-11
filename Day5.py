
n = int(input('Enter the number of strings in the list : '))

str = []
list = []

print('Enter ',n,' strings')
for i in range(0,n):
    str.append(input())

list = str
for i in range(0,len(str)):
    list[i] = str[i][1:]

print('The new list is : ')
print(list)
