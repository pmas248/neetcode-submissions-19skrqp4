class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range( len(temperatures)-1):
            curr_temp = temperatures[i]
            fut_temp = temperatures[i+1]
            count, j = 0, i+1
            while curr_temp >= temperatures[j] and j<len(temperatures)-1:
                print(curr_temp, temperatures[j])
                count += 1
                j = j+1 
            if curr_temp < temperatures[j]:
                count += 1
                res.append(count)
            else:
                res.append(0)

        if temperatures != []:
            res.append(0)
        return res