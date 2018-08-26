class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        nums = []
        ops = []
        i = 0
        n = len(s)
        while i < n:
            if s[i].isdigit():
                val, i = self.getNum(s, n, i)
                nums.append(val)
            elif s[i] == "*":
                val, i = self.getNum(s, n, i + 1)
                nums.append(nums.pop() * val)
            elif s[i] == "/":
                val, i = self.getNum(s, n, i + 1)
                nums.append(int(nums.pop() / val))
            else:
                ops.append(s[i])
                i += 1
                
        result = nums[0]
        while len(ops) > 0:
            op = ops.pop()
            if op == "+":
                result += nums.pop()
            else:
                result -=  nums.pop()
        
        return result
    
    def getNum(self, s, n, i):
        end = i + 1
        while end < n and s[end].isdigit():
            end += 1
        return int(s[i:end]), end