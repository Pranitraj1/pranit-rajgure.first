#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Create a linked list 10-20-30-None
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateLinkedList:
    head = None

    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next

    def CreatNode(self, d):
        n = Node(d)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n


l = CreateLinkedList()
l.CreatNode(10)
l.CreatNode(20)
l.CreatNode(30)
l.printLinkedList()


# In[13]:


# Inserting/Adding elements at the end and at the beginning of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateLinkedList:
    head = None

    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            while self.head is not None:
                print(self.head.data, "--->",end=" ")
                self.head = self.head.next

    def CreatNode(self, d):
        n = Node(d)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head 
            while n.next is not None:
                n = n.next
            n.next = new_node
            
            

            
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node


l = CreateLinkedList()
l.CreatNode(10)
l.CreatNode(20)
l.CreatNode(30)
l.add_end(40)
l.add_begin(5)
l.printLinkedList()
            
            


# In[12]:


# Inserting/Adding Elements after the given in the linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CreateLinkedList:
    head = None
    
    def printLinkedList(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next
        
    def  CreateNode(self,d):
        n = Node(d)
        if self.head is None:
            self.head = n
        else:
            temp = self.head 
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            
    def add_after(self,data,x):
        n = self.head 
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Node is not present in the Linked List")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
            
            
            

l = CreateLinkedList()
l.CreateNode(10)
l.CreateNode(20)
l.CreateNode(30)

l.add_after(50,20)
l.printLinkedList()
            


# In[17]:


# Inseting/Adding elements before the given node in the linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class CreatLinkedList:
    head = None

    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next
    
    def CreatNode(self,d):
        n = Node(d)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head 
            self.head = new_node
            return
        n = self.head 
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
            
        if n.next is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.next = self.head 
            self.head = new_node
            
                
            
            
    
            
l = CreatLinkedList()
l.CreatNode(10)
l.CreatNode(20)
l.CreatNode(30)
l.add_before(5,200)
l.printLinkedList()
            
            
        
        


# In[2]:


# Inserting/Adding elements to the empty linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class CreatLinkedList:
    head = None

    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next
    
    def CreatNode(self,d):
        n = Node(d)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n
    
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

l = CreatLinkedList()

l.insert_empty(10)
l.printLinkedList()
            


# In[4]:


#  Delete the first node in linked list at the beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateLinkedList:
    head = None

    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            while self.head is not None:
                print(self.head.data, "--->",end=" ")
                self.head = self.head.next

    def CreatNode(self, d):
        n = Node(d)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n
    
    
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty so we cant delete nodes!")
        else:
            self.head = self.head.next
            
l = CreateLinkedList()
l.CreatNode(10)
l.CreatNode(20)
l.CreatNode(30)
l.delete_begin()
l.printLinkedList()
            


# In[7]:


# Delete the last node in linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateLinkedList:
    head = None

    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            while self.head is not None:
                print(self.head.data, "--->",end=" ")
                self.head = self.head.next

    def CreatNode(self, d):
        n = Node(d)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n
    
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty so we cant delete nodes!")
        else:
            n = self.head 
            while n.next.next is not None:
                n = n.next 
            n.next = None
            
l = CreateLinkedList()
l.CreatNode(10)
l.CreatNode(20)
l.CreatNode(30)
l.delete_end()
l.printLinkedList()
                        
            


# In[10]:


# Delete any node by vlue in linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateLinkedList:
    head = None

    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            while self.head is not None:
                print(self.head.data, "--->",end=" ")
                self.head = self.head.next

    def CreatNode(self, d):
        n = Node(d)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n
    
    
    def delete_by_value(self,x):
        if self.head is None:
            print("can't delete Linked List is empty!")
            return
        if x==self.head.data:
            self.head = self.head.next
            return
        n = self.head 
        while n.next is not None:
            if x==n.next.data:
                break
            n = n.next
        if n.next is None:
            print("Node is not presnt!")
        else:
            n.next=n.next.next
            
l = CreateLinkedList()
l.CreatNode(10)
l.CreatNode(20)
l.CreatNode(30)
l.delete_by_value(20)
l.printLinkedList()
                     

           


# In[ ]:




