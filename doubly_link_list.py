class Node:
    def __init__(self,perv=None,item=None,next=None):
        self.perv = perv
        self.item = item
        self.next = next
class DLL:
    def __init__(self,start=None):
        self.start = start
    def Is_empty(self):
        return self.start ==None
         
    def Insert_at_start(self, data):
        n = Node(None, data, self.start)
        if self.start is not None:
            self.start.prev = n
        self.start = n
         
    def Insert_at_last(self,data):
        temp = self.start
        n = Node(None,data,None)
        if self.Is_empty():
            self.start = n
        else:
            while temp.next is not None:
                temp=temp.next
            temp.next = n
            n.perv = temp
    def Insert_after(self,item,data):
        if self.Is_empty():
            return None
        temp = self.start
        while temp is not None:
            if temp.item == item:
                n = Node(temp,data,temp.next)
                temp.next= n
            temp = temp.next
        return None
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                print(temp.item)
    def print(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp= temp.next
    def delete_first(self):
        if self.Is_empty():
            return None
        else:
            self.start.next.perv = None
            self.start = self.start.next
    def delete_last(self):
        temp = self.start
        if self.Is_empty():
            return None
        elif self.start.next is None:
            self.start = None
        else:
            while temp.next.next is not  None:
                temp = temp.next        
            temp.next = None 
    def delete_element(self,data):
        temp = self.start
        if self.Is_empty() is None:
            return None
        else:
            while temp.next is not None:
                if temp.next.item == data:
                    temp.next=temp.next.next
                    temp.next.perv = temp
                temp=temp.next
                return None
                
mylist = DLL()
mylist.Insert_at_start(30)
mylist.Insert_at_start(80)
mylist.Insert_at_start(90)
# mylist.print()
mylist.Insert_at_last(50)
mylist.Insert_after(80,100)
mylist.print()
print()
mylist.delete_first()
mylist.delete_last()
mylist.delete_element(100)
mylist.print()

mylist.Insert_at_start(130)
mylist.Insert_at_start(890)
print()
mylist.print()
# mylist.Insert_at_start(30)