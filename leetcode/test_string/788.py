class Solution:
    def rotatedDigits(self, N: int) -> int:
        arr = [3, 4, 7]
        arr2 = [2, 5, 6, 9]
        cnt = 0
        def judge(n):
            res = False
            while n:
                t = n % 10
                if t in arr:
                    return False
                if t in arr2:
                    res = True
                n = n // 10
            return res
        print(judge(20))
        for i in range(N+1):
            if judge(i):
                print(i, end=",")
                cnt += 1
        return cnt
if __name__ == '__main__':
    ret = Solution().rotatedDigits(20)
    print(ret)