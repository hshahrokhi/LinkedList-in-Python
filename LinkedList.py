# -*- coding: utf-8 -*-
"""
@author: Hamed Shahrokhi
"""

# each element of LinkedList is represented with a node that stores data and
# next element in the list
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    
    def __repr__(self):
        return (self.data)


class LinkedList:
    def __init__(self, nodes):
        self.head=None
        
        if nodes is not None:
            node=Node(data=nodes.pop(0))
            self.head=node
            for entry in nodes:
                node.next=Node(data=entry)
                node=node.next
                
        # print(self.__repr__())
        
    def __repr__(self):
        node=self.head
        nodes=[]
        
        while node is not None:
            nodes.append(node.data)
            node=node.next

        return "-->".join(nodes)
    
    # this method is used to insert data at the beggining of LinkedList
    def insert_at_begining(self,data):
        if self.head is None:
            print("this is an empty LinkedList. Adding this entry in")
            self.head=Node(data=data)
            node=self.head
            node.next=None
        else:
            newHead=Node(data=data)
            newHead.next=self.head
            self.head=newHead
            
    # this method is used to insert data at the end of LinkedList        
    def insert_at_end(self,data):
        if self.head is None:
            print("this is an empty LinkedList. Adding this entry in")
            self.head=Node(data=data)
            node=self.head
            node.next=None
        else:
            newNode=Node(data=data)
            node=self.head
            while node.next is not None:
                node=node.next
            node.next=newNode
            newNode.next=None
    
    # this method is used to insert insertValue data after node with afterValue data       
    def insert_after(self,afterValue,insertValue):
        if self.head is None:
            print("this is an empty LinkedList. Adding this entry in")
            return
        node=self.head
        
        while node is not None:
            if node.data==afterValue:
                if node.next is None:
                    self.insert_at_end(insertValue)
                    
                else:
                    newNode=Node(data=insertValue)
                    newNode.next=node.next
                    node.next=newNode
            node=node.next
    
    # this method is used to insert insertValue data before node with beforeValue data        
    def insert_before(self,beforeValue,insertValue):
        if self.head is None:
            print("this is an empty LinkedList. Adding this entry in")
            return
        
        prevNode=self.head
        node=prevNode.next
        if prevNode.data==beforeValue:
            newNode=Node(data=insertValue)
            newNode.next=self.head
            self.head=newNode
            return
        
        while node is not None:
            if node.data==beforeValue:
                newNode=Node(data=insertValue)
                newNode.next=node
                prevNode.next=newNode
            prevNode=node
            node=node.next
    
    # this method is used to delete node with deleteValue data from the LinkedList
    def delete(self,deleteValue):
        if self.head is None:
            print("this is an empty LinkedList. Adding this entry in")
            return
        prevNode=self.head
        node=prevNode.next
        
        if prevNode.data==deleteValue:
            self.head=prevNode.next
            return
        
        while node is not None:
            if node.data==deleteValue:
                prevNode.next=node.next
            prevNode=node
            node=node.next
            
    
# This is for testing all the methods of the LinkedList
hamedLinkedList=LinkedList(["b","c","e","k"])
hamedLinkedList.insert_at_begining("a")
hamedLinkedList.insert_at_end("l")
hamedLinkedList.insert_after("k","a")
hamedLinkedList.insert_before("b","n")
hamedLinkedList.delete("b")