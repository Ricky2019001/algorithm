class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s_len = len(s)
        n = n % s_len
        s = s * 2
        return s[n:n+s_len]


if __name__ == '__main__':
    res = Solution().reverseLeftWords("abcdef", 9)
    print(res)