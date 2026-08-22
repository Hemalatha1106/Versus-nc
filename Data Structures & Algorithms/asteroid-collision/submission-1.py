class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            a=True
            while st and st[-1]>0 and i<0:
                if abs(i)>st[-1]:
                    st.pop()
                elif abs(i)==st[-1]:
                    st.pop()
                    a=False
                    break
                else:
                    a=False
                    break
            if a:
                st.append(i)
        return st