class Stack:

    def __init__(self,capacity) -> None:

        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1 

    def is_stack_overflow(self):
        if self.capacity == self.top + 1:
            print("stack overflow")
            return True
        else:
            return False
        
    def is_stack_underflow(self):
        if self.top == -1:
            print("stack underflow")
            return True
        else:
            return False
        
    def push(self,item):
        if not self.is_stack_overflow():
            self.top += 1 
            self.items[self.top] = item

    def pop(self):
        """remove the last item from top
        """
        #check the underflow > change self.top pointer > 
        if not self.is_stack_underflow():
            temp = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1 
        #TODO  check the size of array if its less than half than reduce the array size to save some space
    def peek(self):
        if not self.is_stack_underflow():
            return self.items[self.top]
    def is_empty(self):
        return self.is_stack_underflow()
    def is_full(self):
        return self.is_stack_overflow()


stack = Stack(2)

stack.push(1)
print(stack.items)
stack.push(2)
print(stack.peek())
print(stack.peek())
print(stack.is_empty())
print(stack.is_empty())
print(stack.is_full())
print(stack.items)
