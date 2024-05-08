def decode_message( s: str, p: str) -> bool:
# write your code here
        lp= len(p)
        ls= len(s)
        dp= [[0]*(ls+1)]*(lp+1)
        dp[0][0]= 1
        for i in range(1, lp+1):
                if(p[i-1]=='*'):
                        j= 0
                        while(j< ls+1):
                                if(dp[i-1][j-1]==1):
                                        break
                                j+=1
                        while(j< ls+1):
                                dp[i][j]=1 
                else:
                        for j in range(1, ls+1):
                                if(p[i-1]=='?' or (p[i-1]== s[j-1])):
                                        dp[i][j]= dp[i-1][j-1]


        return (dp[lp][ls]==1)

print(decode_message('abaacd', 'ab*?c?*'))