def isEmpty(node):
    """
    check if a Node has children or not
    :param node: given node
    :return: true if it hast children and false of don't
    """
    for i in node.children:
        if i is not None:
            return False
    return True


class Node:
    def __init__(self):
        self.children = [None for i in range(10)]
        self.hashedStudent = None


class Trie:
    def __init__(self):
        self.root = Node()
        self.suggestions = []

    def insert(self, key, student):
        """
        add a student using student id in trie and in last node add student hash key
        :param key: student id as key to add in trie
        :param student: student object
        :return:
        """
        curr = self.root
        for i in key:
            # if the child doesnt exist create it
            if curr.children[int(i)] is None:
                curr.children[int(i)] = Node()
            curr = curr.children[int(i)]
        # if its already exists return false
        if curr.hashedStudent is not None:
            return False
        curr.hashedStudent = hash(student)
        return True

    def search(self, key):
        """
        search in trie using a key
        :param key: the student id as key
        :return: hash key if id is available, suggestions if hash is not available but there are other IDs
        and None if there are no student id and no id with that prefix
        """
        curr = self.root
        prefix = ""
        for i in key:
            if curr.children[int(i)] is not None:
                prefix += str(i)
                curr = curr.children[int(i)]
            else:
                # if child is not exist return None
                self.suggestions = []
                self.findSuggestions(curr, prefix)
                return -1, [], None
        # if hash key is available then return the hash key
        if curr is not None and curr.hashedStudent is not None:
            self.suggestions = []
            self.findSuggestions(curr, prefix)
            return 1, self.suggestions, curr.hashedStudent
        # if hash key is not available return list of suggestions
        elif curr is not None and curr.hashedStudent is None:
            self.suggestions = []
            self.findSuggestions(curr, prefix)
            return 2, self.suggestions, None
        else:
            self.suggestions = []
            self.findSuggestions(curr, prefix)
            return -1, [], None

    def findSuggestions(self, curr, prefix):
        """
        method that find suggestions recursively
        :param curr: the Node that we are standing on
        :param prefix: the student id that created till now
        :return:
        """
        # found the leaf
        if curr.hashedStudent is not None:
            self.suggestions.append(prefix)
        # for all of children in given node check the ways to a leaf
        for i in range(10):
            if curr.children[i] is not None:
                self.findSuggestions(curr.children[i], prefix + str(i))

    def remove(self, node, key):
        """
        recursively remove the student id from trie in a bottom-up solution
        :param node: given node
        :param key: key that we want to be deleted
        :return:
        """
        if len(key) == 0:
            node.hashedStudent = None
            return
        self.remove(node.children[int(key[0])], key[1:])
        if isEmpty(node.children[int(key[0])]) is True and node.hashedStudent is None:
            node.children[int(key[0])] = None
