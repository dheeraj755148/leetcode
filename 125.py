import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        s=s.replace(".","")
        s=s.lower()
        new_string = re.sub('[^a-z0-9 \n\.]', '', s)
        print(new_string)
        if new_string==new_string[::-1]:
            return True
        else:
            return False

s = Solution()

print(s.isPalindrome("a."))