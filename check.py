class Solution:
    def checkDivisibility(self, n: int) -> bool:
        real_num=n
        sum=0
        digit_product=1

        while n>0:
            digit=n%10
            sum=sum+digit
            digit_product = digit_product*digit
            n=n//10
        if real_num%(sum + digit_product)==0:
            return True
        else:
            return False        


        