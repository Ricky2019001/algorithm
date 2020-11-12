class Solution:
    def balancedStringSplit(self, s: str) -> int:
        tmp, cnt = 0, 0
        # 判断首字母
        if s[0]=='L':
            s = s.replace('R','A')
            s = s.replace('L', 'R')
            s = s.replace('A','L')

        for i in range(len(s)):
            if s[i]=='R':
                tmp += 1
            if s[i]=='L':
                tmp -= 1
            if tmp == 0:
                cnt += 1
        return cnt
if __name__ == '__main__':
    ret = Solution().balancedStringSplit("RLLRLR")
    print(ret)