class Solution:
    def numUniqueEmails(self, emails: [str]) -> int:
        ret = []
        for email in emails:
            prefix_str = "".join(email[:email.find("@")])
            # print(prefix_str)
            prefix_str = prefix_str.replace('.','')
            # print(prefix_str)
            index = prefix_str.find('+')
            if index == -1:
                print(prefix_str+email[email.find("@"):])
                ret.append(prefix_str+email[email.find("@"):])
            else:
                print(prefix_str[:index]+email[email.find("@"):])
                ret.append(prefix_str[:index]+email[email.find("@"):])
        return len(set(ret))


if __name__ == '__main__':
    ret = Solution().numUniqueEmails(["test.email+alex@leetcode.com"
                                         ,"test.e.mail+bob.cathy@leetcode.com"
                                         ,"testemail+david@lee.tcode.com"])
    print(ret)
