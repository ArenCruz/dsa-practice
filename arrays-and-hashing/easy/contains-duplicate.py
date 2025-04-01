
class Solution(object):
   
    def __init__(self):
        self.exists = {}
        
    def hasDuplicate(self, numbers):
       for num in numbers:
        if num in self.exists:
            return True
        else: 
            self.exists[num] = "added"
       return False
 



numbers = [1,2,3,4]

result = Solution()
print(result.hasDuplicate(numbers))