# August LC Challenge - Day 4
# Power of Four

# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# Follow up: Could you solve it without loops/recursion?

# log num to base 4 - if integer (2.0) true else (2.4) false
# num should be equal to 4 to the power of log value - then true
# Can be done using recursion too 

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num >0 and num == math.pow(4, int(math.log(num, 4))):
            return True
        else:
            return False
        
