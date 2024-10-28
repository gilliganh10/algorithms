

class Fibonacci():

    def __init__(self):
        self.sequence = [0,1]


    def next_number(self) -> list:
        ultimate = self.sequence[-1]
        penultimate = self.sequence[-2]

        self.sequence.append(penultimate+ultimate)

        return self.sequence
    
    def loop(self, steps: int) -> list:

        for _ in range(steps):
            self.sequence = self.next_number()

        return self.sequence
    

fib = Fibonacci()

print(fib.loop(10))



