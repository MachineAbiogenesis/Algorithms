# Stack using linked list
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def display(self):
        print(self.stack)

new_st = Stack()
new_st.push(10)
new_st.push(20)
new_st.push(30)
new_st.display()
print("pop element from stack",new_st.pop())
new_st.display()
print("len of stack ",new_st.length())

'''

[10, 20, 30]
pop element from stack 30
[10, 20]
len of stack  2
'''