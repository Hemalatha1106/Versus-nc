class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def tr(s):
            if s=="9":
                return "0"
            return str(int(s)+1)        
        def tl(s):
            if s=="0":
                return "9"
            return str(int(s)-1)    
        def build(s):
            s=list(s)
            ans=[]
            for n in range(4):
                temp=s[n]
                s[n]=tr(temp)
                ans.append("".join(s))
                s[n]=tl(temp)
                ans.append("".join(s))
                s[n]=temp
            return ans    
        strt="0000"
        q=deque([strt])
        visited={strt}
        deadends=set(deadends)
        d=0
        while q:
            l=len(q)                            
            for i in range(l):
                cur=q.popleft()
                if cur in deadends:
                    continue
                if cur==target:
                    return d
                t=build(cur)
                for e in t:
                    if e not in visited and e not in deadends:
                        q.append(e)
                        visited.add(e)
            d+=1        
        return -1            