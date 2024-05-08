def decode_message( s: str, p: str) -> bool:
# write your code here
        lp= len(p)
        ls= len(s)
        dp= [[0]*(ls+1)]*(lp+1)
        dp[0][0]= 1
        for i in range(1, lp+1):
                for j in range(1, ls+1):
                        if(p[i-1]=='?' or (p[i-1]== s[j-1])):
                                dp[i][j]= dp[i-1][j-1]
                        

        return dp

print(decode_message('abaacd', 'ab*?c?*'))