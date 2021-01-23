class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushBack(self, data):
        """
        a method that find end of a linked list and add a Node after it
        :param data: data that we want to be added in linked list
        :return:
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        """
        found the last node
        """
        tmp.next = node

    def delete(self, data):
        """
        method to remove a data from linked list
        :param data: the data that want to be removed
        :return:
        """
        # first check the special cases
        if data == self.head.data.number:
            self.head = self.head.next
            return
        if data == self.head.next.data.number and self.head.next.next is None:
            self.head.next = None
        tmp = self.head
        while tmp.next is not None:
            if tmp.next.data.number == data:
                tmp.next = tmp.next.next
                return
            tmp = tmp.next

    def search(self, data):
        """
        search for a data in linked lsit
        :param data: the data
        :return:
        """
        node = self.head
        while node is not None:
            if node.data.number == data:
                return node
            node = node.next
        return None

    def getSize(self):
        """
        just for testing the collsion
        :return: size of linked list
        """
        node = self.head
        size = 0
        while node is not None:
            node = node.next
            size += 1
        return size
