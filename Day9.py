
n = int(input('Enter the number of integers in the numbers : '))
print('Enter ',n,' integers')
numbers = [int(input()) for _ in range(n)]
pos = 0
for i in range(n-1):
    if(numbers[i] > numbers[pos]):        
        pos = i

numbers.pop(pos)


high = 0
for i in range(n-2):
    if(numbers[i] > numbers[i+1]):        
        high = numbers[i]

print('The second highest number in the list is : ',high)
