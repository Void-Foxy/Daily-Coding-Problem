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