from bisect import bisect_right
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land = sorted(zip(landStartTime,landDuration), key = lambda x: x[0])
        water = sorted(zip(waterStartTime, waterDuration),  key = lambda x: x[0])

        finishLand = [start+duration for start,duration in land]#[6,9]
        finishWater = [start+duration for start,duration in water]#[9]

        prefixMinLand = [0] * len(land)  #for startLand <= fWater
        prefixMinLand[0] = land[0][1]
        for i in range(1,len(land)):
            prefixMinLand[i] = min(prefixMinLand[i-1],land[i][1])
        
        sufixMinLand = [0] * len(land) #for startLand >  fWater
        sufixMinLand[-1] = finishLand[-1]
        for i in range(len(land)-2,-1,-1):
            sufixMinLand[i] = min(sufixMinLand[i+1],finishLand[i])
        

        prefixMinWater = [0] * len(water) #for startWater <= fLand
        prefixMinWater[0] = water[0][1]
        for i in range(1,len(water)):
            prefixMinWater[i] = min(prefixMinWater[i-1],water[i][1])
        
        suffixMinWater = [0] * len(water) #for startWater > fLand
        suffixMinWater[-1] = finishWater[-1]
        for i in range(len(water)-2,-1,-1):
            suffixMinWater[i] = min(suffixMinWater[i+1],finishWater[i])

        
        landStarts = [l[0] for l in land]
        waterStarts = [w[0] for w in water]
        ans = float('inf')

        #land -> water
        for i in range(len(land)):
            f = finishLand[i]

            indx = bisect_right(waterStarts, f)
            if indx>0:
                ans = min(ans, f + prefixMinWater[indx-1])
            
            if indx < len(water):
                ans = min(ans, suffixMinWater[indx])
        

        #water -> land
        for i in range(len(water)):
            f = finishWater[i]

            indx = bisect_right(landStarts, f)

            if indx > 0:
                ans = min(ans,f+prefixMinLand[indx-1])
            if indx < len(land):
                ans = min(ans, sufixMinLand[indx])
        
        return ans