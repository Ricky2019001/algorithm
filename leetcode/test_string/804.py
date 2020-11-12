class Solution:
    def uniqueMorseRepresentations(self, words: [str]) -> int:
        seret = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        seret_apha = []
        for elem in words:
            str = ""
            for i in range(len(elem)):
                str += seret[ord(elem[i]) - ord('a')]
            seret_apha.append(str)
        return len(set(seret_apha))



if __name__ == '__main__':
    ret = Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    print(ret)