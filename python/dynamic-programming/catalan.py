class CatalanNumbers:

    def __init__(self) -> None:
        pass

    def factorial(self,number):
        
        result = 1

        for i in range(number):
            result = result * (i+1)
    
        return result
    
    def catalan(self,n):

        cn = (self.factorial(2*n)) / (self.factorial(n +1) * self.factorial(n))
        return int(cn)
    
    def catalan_list(self,n):
        # init the array
        result_list = [0] * (n + 1)

        # init the base case
        result_list [0]  =  1

        # loop through the figures for the target

        for i in range(n+1):
            cn_i = self.catalan(i)
            result_list[i] = cn_i
        
        return result_list

    
    def catalan_dp(self, number):

        # init the list
        dp = [0] * (number+1)

        # init the base case
        dp[0] = 1

        for i in range(1,number+1):
            #Recurrence relation
            factor = (2*(2*i - 1))/(i+1)
            dp[i] = int(factor * dp[i-1])
        return dp



        
cn = CatalanNumbers()
print(cn.catalan(5))
print(cn.catalan_dp(5))
print(cn.catalan_list(5))

