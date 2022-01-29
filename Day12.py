
n = int(input("Enter the value of 'n': "))
fiblist = []
a = 0
b = 1
sum = 0
# print("Fibonacci Series: ", end = " ")
for _ in range(1, n + 1):
#   print(sum, end = " ")
  fiblist.append(sum)
  a = b
  b = sum
  sum = a + b
print('The series within the limit ',n,' is ')
print(fiblist)
index = int(input('Enter the index of the number to be searched : '))
print('The number at index ',index,' is = ',fiblist[index])
