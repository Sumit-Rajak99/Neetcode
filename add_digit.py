class Solution:
    def addDigits(self, num: int) -> int:
        sum=0
        while num>0:
            digit=num%10
            sum=sum+digit
            num=num//10
        while sum>=10:
            ans=0
            while sum>0:
                new_digit=sum%10
                ans=ans+new_digit
                sum=sum//10
            sum=ans
        return sum                

        