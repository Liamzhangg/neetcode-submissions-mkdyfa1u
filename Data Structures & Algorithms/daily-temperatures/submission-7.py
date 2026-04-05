class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1):
            j = i + 1
            while j < len(temperatures) and temperatures[i] >= temperatures[j]: 
                if (j == len(temperatures) - 1) and temperatures[j] < temperatures[i]: 
                    result[i] = 0
                
                j += 1

            if j != len(temperatures): 
                result[i] = j - i
            
        return result

            
                 
                    




        

        


        