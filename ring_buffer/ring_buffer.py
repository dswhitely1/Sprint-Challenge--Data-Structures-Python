from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == self.capacity:
            # update the value of the self_current node
            self.current.value = item
            if self.current.next is None:
                while self.current.prev is not None:
                    self.current = self.current.prev
            else:
                self.current = self.current.next
            # Need to find oldest and replace with new value
        # Set self.current to the first oldest.
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        if len(self.storage) < self.capacity and self.current is None:
            self.current = self.storage.head


        # if storage is at capacity
        # Need to remove the oldest


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        cur_list = self.storage.head
        while cur_list is not None and cur_list.next is not None:
            list_buffer_contents.append(cur_list.value)
            cur_list = cur_list.next
        if cur_list:
            list_buffer_contents.append(cur_list.value)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


# buffer = RingBuffer(3)
#
# print(buffer.get())   # should return []
#
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
#
# print(buffer.get())   # should return ['a', 'b', 'c']
#
# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')
#
# print(buffer.get())   # should return ['d', 'b', 'c']
#
# buffer.append('e')
# buffer.append('f')
#
# print(buffer.get())   # should return ['d', 'e', 'f']