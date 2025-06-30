class Solution(object):
    def lengthOfLongestSubstring(self, s):

        l = list(s)

        str = []
        output = []

        for i in l:

            if(i in str):
                test = str[::-1]
                index = len(str) - test.index(i) - 1
                if(len(str) > len(output)):
                    

                    output = str[:]

                str = str[index+1:]

            str.append(i)

        if(len(str) > len(output) and str not in output):
            output = str[:]
        return len(output)

s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))
