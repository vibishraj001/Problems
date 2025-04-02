'''
       "Swap two numbers"

       You are given two numbers a and b. Your task is to swap the given two numbers.

Note: Try to do it without a temporary variable.

GFG SOLUTION :


 class Solution:
    def get(self, a, b):
      # a,b == b,a
        a = a + b
        b = a - b
        a = a - b
        return a ,b



'''
 # SWAPPING OF TWO NUMBER

def swap(a,b):
    print("BEFORE SWAPPING A :",a)
    print("BEFORE SWAPPING B :",b)
    temp = a
    a = b
    b =  temp
    print("AFTER SWAPPING A :",a)
    print("AFTER SWAPPING B :",b)
    return a ,b
swap(5,2)

'''
def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

num1, num2 = 10, 20
num1, num2 = swap(num1, num2)
print("After swapping:", num1, num2)

'''