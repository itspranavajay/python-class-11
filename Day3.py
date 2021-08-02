import math

def main():
    x = int(input('Enter the value of X : '))
    n = int(input('Enter the value of N : '))
    sum = 0.0

    for i in range(1,(2*n)+1,2):
        sum = (x**((2*i)-1)) / (math.factorial(2*i))

    print('The total sum = ',sum)

main()
