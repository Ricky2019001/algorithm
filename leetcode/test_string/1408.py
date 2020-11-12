class Solution:
    def stringMatching(self, words: list) -> list:
        def judgeStr(s1, s2):
            if s1.find(s2) != -1 or s2.find(s1) != -1:
                if len(s1) > len(s2):
                    return True, 0
                return True, 1
            return False, -1
        w = words
        needDel = []
        for i in range(len(w) - 1):
            j = i + 1
            for k in range(j, len(w)):
                res, num = judgeStr("".join(w[i]), "".join(w[k]))
                if res == True:
                    if num == 0:
                        needDel.append(w[i])
                    if num == 1:
                        needDel.append(w[k])
        for i in range(len(needDel)):
            # print(needDel[i])
            words.remove(needDel[i])
        return words

if __name__ == '__main__':
    ret =Solution().stringMatching(["mass","as","hero","superhero"])
    print(ret)
