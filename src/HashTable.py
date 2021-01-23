from LinkedList import LinkedList


class HashTable:
    def __init__(self):
        """
        size of hash table
        """
        self.size = 100
        self.table = [LinkedList() for i in range(self.size)]

    def insert(self, stuobj):
        """
        insert a student in hash table
        :param stuobj: object of student
        :return:
        """
        ll = self.table[hash(stuobj) % self.size]
        ll.pushBack(stuobj)

    def getIndex(self, hcode, studentid):
        """
        method for searching in hash table in average complexity of O(1) and in worst case O(n)
        :param hcode: hash key of student
        :param studentid: student id when collision happened
        :return: return the object of student
        """
        ll = self.table[hcode % self.size]
        return ll.search(studentid)

    def remove(self, hcode, studentid):
        """
        remove a student with given hash key and student id
        :param hcode: hash key of student object
        :param studentid: student id
        :return:
        """
        ll = self.table[hcode % self.size]
        ll.delete(studentid)
