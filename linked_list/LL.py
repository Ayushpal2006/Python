class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = self.head

    def insert_at_last(self, data):
        if self.tail is None:
            self.insert_at_first(data)  # Use self.insert_at_first
            return

        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node  # Correctly update self.tail

    def insert_from_arr(self,arr):
        for i in arr:
            self.insert_at_first(i)

    def get_length(self):
        temp = self.head
        count =0
        while(temp):
            count = count+1
            temp=temp.next
        print(count)
        return count

    def insert(self,data,index):
        size = self.get_length()
        if index==0:
            self.insert_at_first(data)

        if index == size:
            self.insert_at_last(data)

        temp = self.head
        for i in range(0,index-1):
            temp = temp.next

        new_Node = Node(data,temp.next)
        temp.next = new_Node

    def delete_first(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        temp = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

    def delete_last(self):

        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        new_Node  = self.second_last()
        self.tail = new_Node
        self.tail.next = None

    def delete(self,index):
        size = self.get_length()
        if index==0:
            self.delete_first()

        if index==size:
            self.delete_last()

        temp = self.head
        for i in range(0, index - 1):
            temp = temp.next

        temp.next = temp.next.next

    def second_last(self):
        temp = self.head
        count = 0
        while temp.next.next:
            count = count+1
            temp = temp.next

        print(count)
        return temp

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")  # To indicate the end of the list



if __name__ == '__main__':
    l1 = Linked_List()
    arr = [1,2,3,4,5,6]
    l1.insert_at_first(5)
    l1.insert_at_first(6)
    l1.insert_at_last(10)  # Test insertion at the end
    l1.insert_from_arr(arr)  # Test insertion at the end
    l1.insert(100,8)  # Test insertion at the end
    l1.delete_first()
    l1.display()
    l1.get_length()
    l1.second_last()
    l1.delete_last()
    l1.delete(5)
    l1.display()
