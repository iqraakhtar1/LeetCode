class Solution:
    
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while(num > 1):
            if num%2 == 0:  
                counter += 1
            else:
                counter +=2
            num = num//2
        if num == 1:
            counter += 1
        return counter
    
    #One of the ways to solve this problem is by checking how many times we have to divide the given number by 2. If we observe the example, we can see that whenever the division results in an odd number, the counter is incremented by 2, while for an even number the counter is incremented by 1. How can we check if the number is odd or even? Each time we divide the number by 2, we need to check the remainder. If we have a remainder, the number is odd else the number is even.
        
            
        