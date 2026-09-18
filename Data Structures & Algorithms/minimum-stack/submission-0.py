class MinStack:

    def __init__(self):
        self.st = []
        

    def push(self, val: int) -> None:
        min_value = self.getMin()
        if min_value != None:
            if val < min_value:
                min_value = val  
            self.st.append([val, min_value])
        else:
            min_value = val
            self.st.append([val, min_value])
            


    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None
