class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for el in s:
            if el in "([{":
                stack.append(el)
            else:
                if not stack:
                    return False

                if stack[-1] != brackets[el]:
                    return False

                stack.pop()

        return len(stack) == 0
