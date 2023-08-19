class Solution(object):
    def isValid(self, s):
        stack = []
        for character in s:
            if character in '[{(':
                stack.append(character)
            else:
                empty = not stack
                if empty or (character == ']' and stack[-1] != '[') or (character == '}' and stack[-1] != '{') or (character == ')' and stack[-1] != '('):
                    return False
                stack.pop()
        return not stack


