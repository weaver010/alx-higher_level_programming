#!/usr/bin/python3
"""SinglyLinkedList"""


class Node:
    """
    Attributes:
        data: data
    """
    def __init__(self, data, next_node=None):
        """
        Args:
            __data : data
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Returns: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Args:
            value : data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Returns: The next_node instance.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Args:
            value (None): next node of a Node.


        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Attributes:
        head: head
    """
    def __init__(self):
        """
        Args:
            __head : head
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Args:
            value: value.
        """
        n = Node(value)
        if self.__head is None:
            n.next_node = None
            self.__head = n
        elif self.__head.data > value:
            n.next_node = self.__head
            self.__head = n
        else:
            t = self.__head
            while (t.next_node is not None and
                   t.next_node.data < value):
                t = t.next_node
            n.next_node = t.next_node
            t.next_node = n

    def __str__(self):
        """
        Returns: print linked list
        """
        n_d = []
        s = self.__head
        while s:
            n_d.append(str(s.data))
            s = s.next_node
        return ("\n".join(n_d))
