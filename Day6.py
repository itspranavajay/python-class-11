def main():
    n = int(input('Enter an integer : '))
    s = input('Enter a string : ')
    s1 = '0'
    n1 = 0

    for i in s:
        if(i.isdigit()):
            s1 = s1 + i

    n1 = n + int(s1)

    print('Entered number : ',n)
    print('Entered string : ',s)
    print('sum = ',n1)

main()
