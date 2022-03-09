#A regular number in mathematics is defined as one which evenly divides some power of 60.
#Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.
#Given an integer N, write a program that returns, in order, the first N regular numbers.

i = input()
i = int(i)
originali = i
dividerList = []
for x in range(2, i):
  while i%x == 0:
    dividerList.append(x)
    i = i/x
if i == originali:
  print ("Number is prime")
else:
  for x in dividerList:
    print(x, "is a divider")