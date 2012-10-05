from unittest.case import TestCase
from subprocess import call
import sys
import os
import pickle
__author__ = 'hu'

class Win32(TestCase):
   def test_getpath(self):
     # print sys.copyright
      a=[1,10]
      a[len(a):]=[5]
      print a
      print  [x*2 for x in a if x<9]
      print str(type(a))+str(id(a))
      for i in range(*a):
          print i+1
      # notepad= call(["notepad"])
      print sys.modules
      print os.curdir
      f= open("c://temp//test.txt","w+")
      pickle.dump(a,f)
      f.close()
      f= open("c://temp//test.txt","r")
      c=pickle.load(f)
      print a==c
      b=a
      f.close()
      self.te(b)
      print b
      for i in b:
          print b.pop()
      print b
      #for line in f:
      #    print line
      pass

   def te(self,a):
      try:
        a=[3]
        #i=input()
        #print 10/i
      except :
        print sys.exc_info()

