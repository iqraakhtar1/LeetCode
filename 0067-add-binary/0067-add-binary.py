class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result =""
        aLength= len(a)-1
        bLength= len(b)-1
        carry = 0
        while aLength >= 0 or bLength >= 0:
            totalSum = carry
            if aLength >=0:
                totalSum+= int(a[aLength])
                aLength-=1
            if bLength >=0:
                totalSum+= int(b[bLength])
                bLength-=1
            result = str(totalSum % 2) + result
            carry = totalSum // 2
        if carry>0:
            result = str(1)+result
        return result
        