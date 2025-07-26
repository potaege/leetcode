from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:

        output = []

        event_len = []
        event_s = []
        
        event_block = []

        for i in range(0,len(endTime)):
            
            event_len.append(endTime[i] - startTime[i])

            if(i == 0):
                event_s.append(startTime[i] - 0)
            else:
                event_s.append(startTime[i] - endTime[i-1])
                if(i == len(endTime)-1):
                    event_s.append(eventTime - endTime[i])

        max_len = 0
        for i in range(0,len(event_len)):
           
            max_r = event_s[i] + event_s[i+1]
            # แก้นี้
            for j in range(0,len(event_s)):


                if(j != i and j != i+1 and event_len[i] <= event_s[j]):
                    
                    max_r = event_s[i] + event_s[i+1] + event_len[i]
                    break

            if(max_r > max_len):
                max_len = max_r

        
            
        return max_len
    

s =Solution()
print(s.maxFreeTime(41,[17,24],[19,25]))