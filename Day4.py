flag = False

def main():
    lower = int(input('Enter the lower value of the range : '))
    upper = int(input('Enter the upper value of the range : '))

    for i in range(lower,upper+1):
        armstrong(i)
    if(flag == False):
        print('No Armstrong Number found in the range : ',lower,' to ',upper)

def armstrong(n):
    global flag
    n1 = n
    sum = 0
    while (n1 != 0):
        d = n1 % 10
        sum += d**3
        n1 = n1 // 10
    if(n == sum):
        flag = True
        print(n, ' is an Armstrong Number')

main()
