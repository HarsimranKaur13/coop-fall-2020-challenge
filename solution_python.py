class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        arr=[]
        count=0
        max=0
        arr[0]=0
    def add(self, num: int):
        arr[count+1]=arr[count]+num
        max=count+1
        count=count+1;
        print("value: "+str(arr[count]))

    def subtract(self, num: int):
        arr[count + 1] = arr[count] - num
        max=count+1
        count=count+1
        print("value: "+str(arr[count]))

    def undo(self):
        if(count-1>=0):
            count=count-1
        print("value: "+str(arr[count]))

    def redo(self):
        if(count+1<=max):
            count=count+1
        print("value: "+str(arr[count]))

    def bulk_undo(self, steps: int):
        if(count-steps>=0):
            count=count-steps
            print("value: "+str(arr[count]))
        else:
            print("value: "+str(arr[0]))


    def bulk_redo(self, steps: int):
        if(count+steps<=max):
            count=count+steps
            print("value: "+str(arr[count]))
        else:
            print("value: "+str(arr[max]))
