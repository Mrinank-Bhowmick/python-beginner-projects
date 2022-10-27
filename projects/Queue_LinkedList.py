from asyncio.windows_events import NULL


class Node(object):
    def __init__(self, x):
        self.data = x
        self.NextNode = None


class LinkedList(object):
    def __init__(self):
        self.Hnode = None
        self.rear = None

    def Insert(self, x):
        NewNode = Node(x)
        if(self.Hnode is None):
            self.Hnode = NewNode
            self.rear = NewNode
        else:
            self.rear.NextNode = NewNode
            self.rear = NewNode

    def Delete(self):
        tnode = self.Hnode
        if(tnode is not None):
            self.Hnode = self.Hnode.NextNode
            x = tnode.data
            del tnode
            return x

    def PrintList(self):
        tnode = self.Hnode
        while(tnode is not None):
            print(tnode.data, end=" ")
            tnode = tnode.NextNode


class queue():
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.l = LinkedList()

    def enqueue(self, val):
        if(self.front == -1):
            self.l.Insert(val)
            self.front = 0
            self.rear = 0
        else:
            self.l.Insert(val)
            self.rear += 1

    def dequeue(self):
        if(self.front < self.rear):
            print(self.l.Delete(), "is the dequeue element.")
            self.front += 1
        elif(self.front == self.rear and self.front != -1):
            print(self.l.Delete(), "is the deque element.")
            self.front = self.rear = -1
        else:
            print("Queue is empty.")

    def peek(self):
        if(self.front <= self.rear and self.front != -1):
            print(self.l.Hnode.data, "is the first element.")
        else:
            print("Queue is empty.")

    def print(self):
        if(self.front <= self.rear and self.front != -1):
            print("Queue:", end=" ")
            self.l.PrintList()
            print()

        else:
            print("Queue is empty.")


q = queue()
while(1):
    print("1.Enqueue \n2.Dequeue \n3.Peek \n4.Print \n5.Exit \nEnter your choice: ")
    choice = int(input())
    if(choice == 1):
        print("Enter the element: ")
        q.enqueue(int(input()))
    elif(choice == 2):
        q.dequeue()
    elif(choice == 3):
        q.peek()
    elif(choice == 4):
        q.print()
    elif(choice == 5):
        break
    else:
        print("Invalid Input\n")
