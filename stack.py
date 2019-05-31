class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
         
print("Stack in Python..")
stk = Stack()
stk.push(2);
stk.push(4);

print("Stack contains below objects:")
for item in stk.items:
    print (item)
    
print ("Stack Empty : " + str(stk.isEmpty()))

print("Stack size : {} ".format(stk.size()))

print( "Peek : " , stk.peek())

print("Pop : %d " % (stk.pop()))

print( "Peek : " , stk.peek())

print("Stack contains below objects:")
for item in stk.items:
    print (item)

