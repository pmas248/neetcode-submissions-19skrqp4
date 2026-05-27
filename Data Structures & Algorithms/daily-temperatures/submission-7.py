class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #In case no hotter day exists, default=0
        temp = [] #stores tuples (index, temp)

        for i, v in enumerate(temperatures):
            while temp and v > temp[-1][1]: #if stack is empty and if curr > head
                day, tmp = temp.pop()
                res[day] = i - day
            temp.append((i, v)) 
        return res