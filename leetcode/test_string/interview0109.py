class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if (len(s1) == 0 and len(s2) != 0) or (len(s2) == 0 and len(s1) != 0):
            return False
        s1 = s1 * 2
        return s1.find(s2) != -1

if __name__ == '__main__':
    ret = Solution().isFlipedString("rxOpSEXvfIuoRJfjwgwuomevMMBOfeSMvYSPBaovrZBSgmCrSLDirNnILhARNShOYIFBHIRiFKHtfxWHjawaLRAEYPIZokUKgiqyZpvcOHdfPpRqHADKAXzEfzhxdXXb","")
    print(ret)