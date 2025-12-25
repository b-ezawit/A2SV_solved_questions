class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        pop_changes = [0] * 101
        
        for birth, death in logs:
            pop_changes[birth - 1950] += 1 
            pop_changes[death - 1950] -= 1 
            
        max_pop = 0
        earliest_year = 1950
        current_pop = 0
        
        for i in range(101):
            current_pop += pop_changes[i]
            
            if current_pop > max_pop:
                max_pop = current_pop
                earliest_year = 1950 + i
                
        return earliest_year