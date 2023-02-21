#!/usr/bin/env python

from base import synthetic_generation
import sys

def iter(a, b, c, d, e, f, n=0):
    for inc in range(0, n):
        synthetic_generation(
          a,
          b,
          c,
          d,
          e,
          f,
          inc
        )

if __name__ == "__main__":
    iter(
      str(sys.argv[1]),
      str(sys.argv[2]),
      int(sys.argv[3]),
      int(sys.argv[4]),
      float(sys.argv[5]),
      str(sys.argv[6]),
      int(sys.argv[7])
    )


