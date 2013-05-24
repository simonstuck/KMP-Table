#!/usr/bin/python

from array import *
import sys

def kmp(P):
  m = len(P)
  n = []
  n.append(0)

  k = 0;
  for q in range(1,m):
    while k>0 and P[q] != P[k] :
      k = n[k-1]

    if P[q] == P[k]:
      k += 1

    n.append(k)
  return n

res = kmp(sys.argv[1])
print res

