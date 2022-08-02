from coba1 import average
import unittest

class  TestAverage(unittest.TestCase):

     def test1(self):
         self.assertEqual(average(0,2,4),2)

     def test2(self):
         self.assertEqual(average(-1,-1,-1),1)

     def test3(self):
         self.assertEqual(average(2.33,2.33,2.33),2.33)

print(f"avrg = {average(0,2,4)}")
if __name__ == '__main__':
   unittest.main()
