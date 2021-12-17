class Stack:
    def __init__(self):
        self.stack=[];    
    def stack_push(self,element):
        self.stack.append(element)
    def stack_pop(self):
        return self.stack.pop() if self.is_stack_empty()!=0 else -1 
    def stack_top(self):
        return self.stack[0] if self.is_stack_empty()!=0 else -1 

    def is_stack_empty(self):
        return 1 if len(self.stack)!=0 else 0  



stack=Stack()
stack.stack_push('jilan')
print(stack.stack_pop())
print(stack.stack_pop())

