
n = int(input('Enter the number of integers in the numbers : '))
numbers = []

print('Enter ',n,' integers')
for i in range(0,n):
    numbers.append(int(input()))


pos = 0
for i in range(0,n-1):
    if(numbers[i] > numbers[pos]):        
        pos = i

numbers.pop(pos)


high = 0
for i in range(0,n-2):
    if(numbers[i] > numbers[i+1]):        
        high = numbers[i]

print('The second highest number in the list is : ',high)
