
n = int(input("Enter the value of 'n': "))
fiblist = []
a = 0
b = 1
sum = 0
count = 1
# print("Fibonacci Series: ", end = " ")
while(count <= n):
#   print(sum, end = " ")
  fiblist.append(sum)
  count += 1
  a = b
  b = sum
  sum = a + b
print('The series within the limit ',n,' is ')
print(fiblist)
index = int(input('Enter the index of the number to be searched : '))
print('The number at index ',index,' is = ',fiblist[index])
