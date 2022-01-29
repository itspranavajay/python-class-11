
n = int(input('Enter the number of strings in the list : '))

list = []

print('Enter ',n,' strings')
str = [input() for _ in range(n)]
list = str
for i in range(len(str)):
    list[i] = str[i][1:]

print('The new list is : ')
print(list)
