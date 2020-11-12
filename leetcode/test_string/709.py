class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

if __name__ == '__main__':
    ret = Solution().toLowerCase("MAKE")
    print(ret)