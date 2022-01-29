
def main():
    
    for i in range(5,-1,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()

    n = int(input('Enter the value of N : '))
    for k, i in enumerate(range(1,n+1), start=65):
        for _ in range(1,i+1):
            print(chr(k),end=" ")
        print()

    n = int(input('Enter the value of N : '))
    k1 = 97
    k2 = 1
    l1 = 1
    l2 = 2
    for i in range(1,n+1):
        if (i % 2 != 0):
            for _ in range(1,l1+1):
                print(chr(k1),end=' ')
                k1 += 1
            l1 += 2
        else:
            for _ in range(1,l2+1):
                print(k2,end=' ')
                k2 += 1
            l2 += 2

        print()
        
main()
