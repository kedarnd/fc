import unittest

def next_permutation(s):
    sl=list(s)
     
    for i in range(len(sl)-1,0,-1):
      if sl[i-1]>=sl[i]:
           continue
      else:
           for j in range(i,len(sl)):
               if (sl[j]>sl[i-1]):
                continue
               else:
                break
           if sl[j]>sl[i-1]:
            tmp=sl[i-1]
            sl[i-1]=sl[j]
            sl[j]=tmp
           else:
            tmp=sl[i-1]
            sl[i-1]=sl[j-1]
            sl[j-1]=tmp

            
           k=sl[i:]
           k.sort()
           sl=sl[:i]+k
           return ''.join(sl)

def push_to_right(l,i):
    for j in range(len(l)-1,i,-1):
        l[j]=l[j-1]
    return l



class TestStringMethods(unittest.TestCase):
#tests a regular case
    def test_next_permutation1(self):
        self.assertEqual(next_permutation("34251"), "34512")
#tests a corner case
    def test_nextpermutation2(self):
        self.assertEqual(next_permutation("4321"), None)
#tests a regular case
    def test_push_to_right1(self):
        self.assertEqual(push_to_right([1,2,3,4,5,6],2), [1,2,3,3,4,5])
#tests a corner case
    def test_push_to_right2(self):
        self.assertEqual(push_to_right([1,2,3,4,5,6],5), [1,2,3,4,5,6])




if __name__ == '__main__':
    unittest.main()
