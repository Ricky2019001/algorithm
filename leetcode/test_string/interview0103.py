class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        cnt = S[:length].count(" ")
        print(cnt)
        return S.replace(" ", "%20")[:length + 2 * cnt]


if __name__ == '__main__':
    ret = Solution().replaceSpaces("Mr John Smith    ",13)
    print(ret)