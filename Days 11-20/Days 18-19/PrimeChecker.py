import numpy
N = int(input())

if N>2 and N%2 == 0:print("Not a prime")
else:
  for i in numpy.arange(2,N**(1/2)):
    if N%i == 0:pass
  print("Prime")
