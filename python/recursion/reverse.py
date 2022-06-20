lass Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        m = len(s)
        for i in range ( m // 2):
           r = s[i]
           s[i] = s[m-i-1]
           s[m-i-1] = r
        s = ''.join(s)
        print(s)

if __name__ == "__main__":
    
