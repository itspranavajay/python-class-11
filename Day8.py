
n = int(input('Enter the number of elements in the list : '))
numbers = []

for i in range(n):
    numbers.append(int(input('Enter an integer : ')))

for num in numbers:
    if(num > 0 and num %2 == 0):
        print(num,' : after operation : ',(num/2))
    elif(num < 0 and num % 2 != 0):
        print(num,' : after operation : ',(num**2))
    else:
        print(num,' : after operation : ',(num**3))
