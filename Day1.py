import math

def main():
    print('1. Minutes to hours Calculator')
    print('2. Compute GCD and LCM of 2 integers')
    print('0. To Exit')
    uc = int(input('Enter your choice : '))

    if(uc == 1):
        mins = int(input('Enter the number of minutes : '))
        hours = mins // 60
        min = mins % 60
        print(hours,' hour(s)',min,' minute(s)')
    elif(uc == 2):
        n1 = int(input('Enter the first number : '))
        n2 = int(input('Enter the second number : '))
        hcf = math.gcd(n1,n2)
        lcm = math.lcm(n1,n2)
        print('GCD = ',hcf)
        print('LCM = ',lcm)
    elif(uc == 0):
     	return
    else:
        print('Wrong number entered, please try again !!')
    print('\n\n')
    main()

main()
