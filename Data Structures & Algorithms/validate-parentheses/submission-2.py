class Solution:
    def isValid(self, s: str) -> bool:
        d={"]":"[",")":"(","}":"{"}
        st=[]
        for i in s:
            if i in d:
                if st and st[-1]==d[i]:
                    st.pop()
                else:
                    return False        
            else:
                st.append(i)
        return st==[]            