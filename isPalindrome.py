class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        refined_string = ""

        for character in s:
            if character.isalnum():
                refined_string += character
        refined_string = refined_string.lower() 
        
        ptr1 = 0
        ptr2 = len(refined_string) - 1

        while ptr1 <= ptr2:
            if refined_string[ptr1] != refined_string[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1
        
        return True

sol = Solution()
string = "A man, a plan, a canal: Panama"
sol.isPalindrome(string)
