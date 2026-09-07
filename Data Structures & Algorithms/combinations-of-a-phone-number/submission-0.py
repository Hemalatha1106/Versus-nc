class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res=[]
        def dfs(ind,l):
            if len(l)==len(digits):
                if l:
                    res.append(l)
                return
            for i in range(ind,len(digits)):
                for ch in d[int(digits[i])]:
                    dfs(i+1,l+ch)
        dfs(0,"")
        return res
