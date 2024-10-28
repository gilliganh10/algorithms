import time

class Factorials:
    def __init__(self) -> None:
        pass
        
    def factorial(self,target:int) -> list:
        
        # init number 1
        target_list = [0] * (target+1)
        target_list[0] = 1

        result = 1

        # Loop through the rest of the target
        for i in range(1,target+ 1):
            result = result * (i)
            target_list[i] = result

        return target_list
        
    def factorial_dp(self,target: int) -> list:
        # Init the list
        dp_array = [0] * (target+1)

        # init the base cases for 0 and 1
        dp_array[0] = 1
        dp_array[1] = 1
        # loop through the rest of factors:
        for i in range(2, target+1):
            dp_array[i] = i * (dp_array[i-1])

        return dp_array
    

f = Factorials()


target = 100000

# Time factorial(11)
start_time = time.time()
f.factorial(target)
end_time = time.time()
print(f"Time for normal Calculation ({target}):", end_time - start_time, "seconds")



# Time factorial_dp(11)
start_time = time.time()
f.factorial_dp(target)
end_time = time.time()
print("Time for factorial_dp(11):", end_time - start_time, "seconds")
