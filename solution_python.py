
class EventSourcer():
    count = 0
    arr = []
    arr.append(0)
    max = 0

    # Do not change the signature of any functions
    def __init__(self):
        self.value = 0

    def add(self, num: int):
        self.arr.append(self.arr[self.count]+num)
        if(self.max<self.count+1):
            self.max=self.count+1
        self.count=self.count+1
        print(str(self.arr[self.count]))

    def subtract(self, num: int):
        self.arr.append(self.arr[self.count] - num)
        if(self.max<self.count+1):
            self.max=self.count+1
        self.count=self.count+1
        print(str(self.arr[self.count]))

    def undo(self):
        if(self.count-1>=0):
            self.count=self.count-1
        print(str(self.arr[self.count]))

    def redo(self):
        if(self.count+1<=self.max):
            self.count=self.count+1
        print(str(self.arr[self.count]))

    def bulk_undo(self, steps: int):
        if(self.count-steps>=0):
            self.count=self.count-steps
            print(str(self.arr[self.count]))
        else:
            print(str(self.arr[0]))


    def bulk_redo(self, steps: int):
        if(self.count+steps<=self.max):
            self.count=self.count+steps
            print(str(self.arr[self.count]))
        else:
            print(str(self.arr[self.max]))
