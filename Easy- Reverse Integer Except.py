class Solution:
    def reverse(x):
           try:
             if x >=0:
               rev_int = str(x)[-1::-1]
               rev_int = rev_int.lstrip("0")  
             else:
               rev_int = str(x)[-1:0:-1]
               rev_int = rev_int.lstrip("0")
               rev_int = "-" + rev_int
             if (abs(int(rev_int)) > (2**31 - 1)):
                  return 0
             return rev_int 
           except ValueError:
                  return 0    
if __name__ == '__main__': ## This is a good learning -> That we need to use double underscore over here.        
    int_val = -2**32
    %timeit Solution.reverse(int_val)
#    print(Solution.reverse(int_val))     