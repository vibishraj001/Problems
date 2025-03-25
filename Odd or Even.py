'''
  ---Odd or Even--
Given a positive integer n, determine whether it is odd or even.
 Return true if the number is even and false if the number is odd.


 GFG SOLUTION

def isEven(self,n):
    if (n % 2 == 0):
        return True
    else :
        return False

'''

#MY SOLUTION

#IF GIVEN NUMBER IS ODD OR EVEN
def is_Even (n):
    return n % 2 ==0
if __name__ == "__main__":
    n= int (input("Enter a  n value :"))
    if is_Even(n):
        print (n,": Even")
    else :
        print(n,": odd")