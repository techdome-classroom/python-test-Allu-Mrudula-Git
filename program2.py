def decode_message( s: str, p: str) -> bool:
# write your code here
        lp= len(p)
        ls= len(s)
        dp= [[0]*(ls+1)]*(lp+1)
        for i in range(ls)
        return dp

print(decode_message('abaacd', 'ab*?c?*'))