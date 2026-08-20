class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=Counter(chars)
        res=0
        for i in words:
            w=Counter(i)
            f=True
            for ch in w:
                if ch not in c or w[ch]>c[ch]:
                    f=False
            if f:
                res+=len(i)
        return res                 