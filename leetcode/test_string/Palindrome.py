# check out Palindrome
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(lft, rgh):
            while lft < rgh:
                if s[lft] != s[rgh]:
                    return False
                lft += 1
                rgh -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return check(left + 1, right) or check(left, right - 1)
        return True

if __name__ == '__main__':
    ret = Solution().validPalindrome("eeccccbebaeeabebccceea")
    print(ret)