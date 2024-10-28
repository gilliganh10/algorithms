def climb_stairs(number_of_steps: int) -> int:
    """
    LeetCode No.70: Climbing Stairs
    Distinct ways to climb a number_of_steps staircase where each time you can either
    climb 1 or 2 steps.

    Args:
        number_of_steps: number of steps on the staircase

    Returns:
        Distinct ways to climb a number_of_steps staircase

    Raises:
        AssertionError: number_of_steps not positive integer
    """
    assert (
        isinstance(number_of_steps, int) and number_of_steps > 0
    ), f"number_of_steps needs to be positive integer, your input {number_of_steps}"
    

    # Base case of 1 step
    if number_of_steps == 1:
        return 1
    
    # Init base for 2 steps, where you 
    previous, current = 1, 1 

    for _ in range(number_of_steps - 1):
        previous,current = current + previous, previous

    return current


print(climb_stairs(4))

"""
1 step:
    1 way
2 step:
    2 ways: 1 + 1, 2
3 step:
    2 ways: 1+1+1, 2+ 1
4 step:
    3 ways: 1+1+1+1, 2+2, 1+1+2



"""