class MinStack:

    def __init__(self):
        self.stack = []
        self.min_prefix = []
        self.curr_min = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_prefix or val < self.min_prefix[-1]:
            self.min_prefix.append(val)
        
        else:
            self.min_prefix.append(self.min_prefix[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_prefix.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_prefix[-1]

# [-2,0, 2,]

#[-2,-2, -2,]
        

        
