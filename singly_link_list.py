class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        if self.start is None:
            return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start= n
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            self.start = n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next= n
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item  == data:
                return temp
            temp=temp.next 
        return None
    def insert_item(self,item,data):
        if self.start is None:
            return None
        else:
            temp = self.start
            while temp is not None:
                if temp.item == item:
                    n = Node(data,temp.next)
                    temp.next = n
                temp = temp.next
            return None
    def print(self):
        temp = self.start
        while temp is not None:
            print(temp.item , end=" ")
            temp=temp.next
    def delete_first(self):
        if self.start is None:
            return None
        else:
            self.start = self.start.next
    def delete_item(self,data):
        if self.start is None:
            return None
        elif self.start.next is None:
            if self.start.item == data:
                self.start=None
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.item == data:
                    temp.next = temp.next.next
                temp = temp.next
            return None 
    def delete_last(self):
        if self.start is None:
            return None
        elif self.start.next is None:
            self.start=None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    
mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(15620)
mylist.insert_at_last(50)
mylist.insert_at_last(80)
mylist.insert_at_last(60)
print(mylist.search(50).item)
mylist.insert_item(20,100)
mylist.insert_item(100,125)
mylist.print()
# mylist.delete_first()
print()
# mylist.delete_last()
mylist.delete_item(125)
mylist.print()
    