class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ind=0
        for i in logs:
            c=i[:-1]
            if c=="..":
                if ind>0:
                    ind-=1
            elif c==".":
                continue
            else:
                ind+=1
        return ind                   
                