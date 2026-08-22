class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        num=0
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i=="[":
                st.append(num)
                st.append("")
                num=0
            elif i=="]":
                ch=st.pop()
                m=st.pop()
                d=ch*m
                if st:
                    st[-1]+=d
                else:
                    st.append(d)
            else:
                if st:
                    st[-1]+=i
                else:
                    st.append(i)                     
        return st[0]              