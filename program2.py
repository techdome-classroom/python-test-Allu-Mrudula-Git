def decode_message( s: str, p: str) -> bool:
# write your code here
        lp= len(p)
        ls= len(s)
        dp= [[0]*(ls+1)]*(lp+1)
        dp[0][0]= 1
        for i in range(lp+1):
                
        return dp

print(decode_message('abaacd', 'ab*?c?*'))