# in py lists, if element inserted in middle,
# swaps made to make space

# linked list:
# insertion/delete begin O(1)
# Insert/delete middle O(n)

# but traversal O(n) not O(1) [in array]

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head

        while itr.next!=None:
            itr = itr.next
        
        itr.next = Node(data,None)

    def insert_from_list(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self,index):
        if index == 0:
            self.head = self.head.next
            print("Removed")
            # auto garbage collection
            # don't need "free(temp)"
            return

        itr = self.head

        c = 0
        while itr:
            if c == index-1:    # prev node
                itr.next = itr.next.next
                print("Removed")
                return
            itr = itr.next
            c+=1

        print("Beyond scope")

    def insert_at(self,index,data):
        if index == 0:
            self.insert_at_beg(data)
            print("Inserted")
            return

        itr = self.head

        c=0
        while itr:
            if c == index - 1:
                node = Node(data,None)
                node.next = itr.next
                itr.next = node
                print("Inserted")
                return
            
            itr = itr.next
            c+=1

        print("Error")

    def print_(self):
        if self.head is None:
            print("Empty")
            return
        
        itr = self.head

        while itr.next!=None:
            print(itr.data,"-->",end=" ")
            itr = itr.next
        
        print(itr.data)

    # Exercise
    # 1
    def insert_by_value(self,prev,data):
        if self.head is None:
            insert_by_value(data)
            print("First element")
            return

        itr = self.head

        while itr and itr.data!=prev:
            itr = itr.next

        if itr is None:
            print("Prev not found")
            return

        node = Node(data,None)
        node.next = itr.next
        itr.next = node
        print("Inserted")

    # 2
    def remove_by_value(self,data):
        if self.head is None:
            print("Empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            print("Removed")
            return

        itr = self.head
        itr2 = self.head

        while itr and itr.data!=data:
            itr2 = itr
            itr = itr.next

        if itr is None:
            print("Not found")
            return

        itr2.next = itr2.next.next
        print("Removed")

l = LinkedList()
l.print_()
l.insert_at_beg(3)
l.insert_at_beg(5)
l.insert_at_beg(6)
l.print_()
l.insert_at_end(9)
l.insert_at_end(12)
l.print_()
L = [1,7,8,6,3]
l.insert_from_list(L)
l.print_()
print(l.head.data)
print(l.head.next.next.data)
l.remove_at(5)
l.remove_at(20)
l.print_()
l.insert_at(3,45)
l.print_()
l.insert_at(0,13)
l.print_()
l.insert_by_value(45,90)
l.print_()
l.insert_by_value(0,90)
l.print_()
l.remove_by_value(45)
l.print_()
l.remove_by_value(91)
l.print_()
l.remove_by_value(13)
l.print_()
