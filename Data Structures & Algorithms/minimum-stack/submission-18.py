class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        if not self.stack or not self.mini:
            self.stack.append(val)
            self.mini.append(val)
        else:
            self.stack.append(val)
            self.mini.append(val)
            self.mini.append(min(self.mini[-2], val))

    def pop(self) -> None:
        if not self.stack or not self.mini:
            return 
        else: 
            self.stack.pop()
            if len(self.mini) == 1:
                self.mini.pop()
            else:
                self.mini.pop()
                self.mini.pop()
        

    def top(self) -> int:
        if not self.stack or not self.mini:
            return 0 
        else:
            return (self.stack[-1])
        

    def getMin(self) -> int:
        return (self.mini[-1])
        
