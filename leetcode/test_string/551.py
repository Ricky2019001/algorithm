class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1:
            return False
        num = s.find('LLL')
        if num == -1:
            return True
        return False

if __name__ == '__main__':
    ret =Solution().checkRecord("PPALLL")
    print(ret)