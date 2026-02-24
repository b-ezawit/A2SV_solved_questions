class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hmap = {}
        for s in cpdomains:
            dots = s.count(".")
            s = s.split()
            for _ in range(dots+1):
                if s[1] not in hmap:
                    hmap[s[1]] = int(s[0])
                else:
                    hmap[s[1]] += int(s[0])

                if "." in s[1]:
                    dot_indx = s[1].find(".")
                    s[1] = s[1][dot_indx+1:]        
        return [f"{val} {key}" for key,val in hmap.items()]
                

        
        