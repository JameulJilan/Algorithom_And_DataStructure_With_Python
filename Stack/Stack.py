import sys

class Stack:
    def __init__(self):
        self.stack=[];    
    def stack_push(self,element):
        self.stack.append(element)
    def stack_pop(self):
        return self.stack.pop()
    def stack_top(self):
        return self.stack[len(self.stack)-1]
    def is_stack_empty(self):
        return True if len(self.stack)==0 else False  


def numbers_to_strings(argument):
    switcher = {
        "1": "Push",
        "2": "Pop",
        "3": "Top",
        "4": "Exit",
    }

    return switcher.get(argument, "Default")



stack=Stack()

while(True):
    print('1: Push')
    print('2: Pop')
    print('3: Top')
    print('4: Exit')
    print('Enter Your Option : ')
    choice = input()

    if(numbers_to_strings(choice)=='Push'):
         print('Enter Your Value : ')
         value=input()
         stack.stack_push(value)

    elif(numbers_to_strings(choice)=="Pop"):
        if(stack.is_stack_empty()):           
            print('Stack Is Empty')
        else:
            print(stack.stack_pop())

    elif(numbers_to_strings(choice)=="Top"):
        if(stack.is_stack_empty()):
            print('Stack Is Empty')
        else:
            print(stack.stack_top())

    elif(numbers_to_strings(choice)=="Exit"):
        sys.exit()
    else:
        print('Envalid Input.')
        

