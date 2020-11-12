class Solution:
    def thousandSeparator(self, n: int) -> str:
        str = "".join('%d' %n)
        return self.strSplit(str)

    def strSplit(self, s: str) -> str:
        if len(s) <= 3:
            return s
        s = s[::-1]
        res = ""
        for i in range(len(s)):
            if i == 0:
                res += s[0]
            elif i % 3 == 0:
                res = s[i] + "." + res
            else:
                res = s[i] + res
        return res


if __name__ == '__main__':
    ret = Solution().thousandSeparator(1234)
    print(ret)
