"""
    There are three kinds of linked lists:
    > Singly linked lists
      Each element in the linear list has a pointer
      to the next element.
      We should know the first element pointer to be able to traverse the list.
      It can only be traversed from the head.

    > Doubly linked lists
      Each element has a link to previous as well as the next element.

    > Circular linked lists
      This is a variation tha might be either singly or doubly list. It does
      not have the end and the last element points to the first element.

    Problems with linked lists.
    1. Tracking the head element.
    2. Always test for the end of a linked list as you traverse it.
    3. Traversing the list
    4. Adding and deleting the elements
"""

###############################################################
# Singly Linked Lists                                         #
###############################################################
class SListElement:
    """
    Singly linked list implementation
    """
    def __init__(self, data=None, next_element=None):
        self.data = data
        self.next_element = next_element

    def set_value(self, data):
        self.data = data

    def set_next(self, next_element):
        self.next_element = next_element

    def get_next(self):
        return self.next_element

    def value(self):
        return self.data

    def __str__(self):
        return str(self.data)

class SLinkedList:
    """
    This object describes singly linked list and provides
    methods for it.
    """
    def __init__(self):
        # Create a head element and keep track of it
        self.head = None
        self.el_num = 0

    def get_head(self):
        """
        Returns the reference to the head element
        :return:
        """
        return self.head

    def get_length(self):
        """
        Returns the length of the list
        :return:
        """
        return self.el_num

    def insert_element(self, data):
        """
        This method inserts list element in front of the list
        and it becomes a new head
        :param data:
        :return:
        """
        list_element = SListElement(data)
        list_element.set_next(self.head)
        self.head = list_element
        self.el_num += 1

    def print_list(self):
        """
        This method prints the linked list
        :return:
        """
        element = self.head
        while element:
            print element.value()
            element = element.get_next()

    def find_element(self, data):
        """
        This method traverses the list from the head element
        and returns the reference to the element that contains
        matched data. If data is not found, a None is returned.
        :param data:
        :return:
        """
        element = self.head
        while element and data != element.value():
            element = element.get_next()

        return element

    def insert_after(self, element_to_insert_after, data):
        """
        This routine inserts the element after the specified
        element. If specified element is not found it will
        insert the element to the head.
        :param element:
        :param data:
        :return:
        """
        # Special case when list is empty or the matching element
        # is a head element
        if self.head is None or self.head == element_to_insert_after:
            self.insert_element(data)
            return

        element = self.head.get_next()
        while element:
            if element == element_to_insert_after:
                new_element = SListElement(data)
                new_element.set_next(element.get_next())
                element.set_next(new_element)
                self.el_num += 1
                return

        # If we got here, the element was not found and therefore
        # we insert it in front of the list
        self.insert_element(data)
        return

    def delete_element(self, element_to_delete):
        """
        This method deletes the element from the list
        by the reference
        :param data:
        :return: status of deletion: True if found and deleted.
        """
        # Check if list is not empty and the element requested
        # to be deleted is not Null
        if self.head is None or element_to_delete is None:
            return False

        # Start list traversal from teh head element
        # Consider a special case for the head element
        if self.head == element_to_delete:
            self.head = element_to_delete.get_next()
            self.el_num -= 1
            return True

        element = self.head
        # Traverse the list
        while element:
            # Check if current element is the element to be deleted
            if element.get_next() == element_to_delete:
                # Reassign the element to the next one
                element.set_next(element_to_delete.get_next())
                self.el_num -= 1
                return True
            element = element.get_next()

        # Element is not found
        return False

    def clear(self):
        """
        This method clears the entire list
        :return:
        """
        element = self.head
        while element:
            next_element = element.get_next()
            self.delete_element(element)
            element = next_element

    # Stack-like routines to push and pop to the list
    def push(self, data):
        """
        Inserts the element to the list in front.
        :param data:
        :return:
        """
        self.insert_element(data)

    def pop(self):
        """
        Returns the data for the last element and deletes it
        :return:
        """
        if self.head is None:
            return None
        data = self.head.value()
        self.delete_element(self.get_head())
        return data


###############################################################
# Doubly Linked Lists                                         #
###############################################################
class DListElement:
    """
    This class describes a doubly linked list element
    """
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def set_value(self, data):
        self.data = data

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def value(self):
        return self.data

    def __str__(self):
        return str(self.data)


class DlinkedList:
    """
    This class describes doubly linked list and
    its methods.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_head_element(self, data):
        """
        Inserts a head element
        :param data:
        :return:
        """
        new_element = DListElement(data)
        # Check for empty list condition
        if self.head is None:
            self.head = new_element
            # also the tail element is the head at this point
            self.tail = new_element
        else:
            # Otherwise append it in front
            new_element.set_right(self.head)
            self.head.set_left(new_element)
            self.head = new_element

        # Increment list length
        self.length += 1
        return


    def insert_tail_element(self, data):
        """
        This method inserts the tail element
        :param data:
        :return:
        """
        new_element = DListElement(data)
        # Consider a special case when the list is empty
        if self.tail is None:
            self.tail = new_element
            # Also update the head element
            self.head = new_element
        else:
            new_element.set_left(self.tail)
            self.tail.set_right(new_element)
            self.tail = new_element

        self.length += 1
        return

    def find_element(self, data):
        pass

    def insert_after(self, element, data):
        pass

    def insert_before(self, element, data):
        pass

    def print_from_head(self):
        """
        This method traverses the list from head to tail and
        prints its elements
        :return:
        """
        element = self.head
        while element:
            print(element.value())
            element = element.get_right()

        return

    def print_from_tail(self):
        """
        This method traverses the list from head to tail and
        prints its elements
        :return:
        """
        element = self.tail
        while element:
            print(element.value())
            element = element.get_left()

        return

###############################################################
# Multi-Level Doubly Linked Lists
###############################################################
class MDListElement:
    """
    This class describes a doubly linked list element
    """

    def __init__(self, data=None, left=None, right=None, child=None):
        self.data = data
        self.left = left
        self.right = right
        self.child = child

    def set_value(self, data):
        self.data = data

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_child(self):
        return self.child

    def set_child(self, child):
        self.right = child

    def get_right(self):
        return self.right

    def value(self):
        return self.data

    def __str__(self):
        return str(self.data)


class MDLinkedList:
    """
    This class describes nulti-level doubly linked list
    structure and its methods
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_head_element(self, data):
        pass

    def insert_tail_element(self, data):
        pass

    def find_element(self, data):
        pass


if __name__=="__main__":
    sl = DlinkedList()
    sl.insert_tail_element(1)
    sl.insert_tail_element(2)
    sl.insert_tail_element(3)
    sl.insert_tail_element(4)
    sl.print_from_head()







