#
# Python-3
#
import sys
import pandas
import numpy as np

def testprint(i,s):
    # print(">> Test " + str(i) + ": " + str(s))
    # let's use formatted string instead:
    print(f">> Test {i}: {s}")

testprint(1,sys.path)
testprint(2,"Hello wolrd!")
testprint(3,1 + 10)

def foo():
   return "Foo says: Hello wolrd!"

testprint(4,foo())

array = np.zeros((3,3))

testprint(5,array)
