class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for i in strs:
            a=''.join(sorted(i))
            # print(a)
            x=mp.get(a,[])
            y=x.append(i)
            # print(y)
            mp[a]=x
            # print(x,mp)
        return mp.values()
            
        
