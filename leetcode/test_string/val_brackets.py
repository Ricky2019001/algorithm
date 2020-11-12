class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"(":")","[":"]","{":"}"}
        stack = []
        for i in range(len(s)):
            if s[i] in dict:
                stack.append(s[i])
            elif len(stack) != 0 and dict[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False
        return stack == []


if __name__ == '__main__':
    ret = Solution().isValid("([)]")
    print(ret)