class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ["[", "{", "("]:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    curr_char = stack.pop()

                    if curr_char == "[" and char != "]":
                        return False
                    if curr_char == "{" and char != "}":
                        return False
                    if curr_char == "(" and char != ")":
                        return False
        
        if stack:
            return False
        return True