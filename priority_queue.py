
class PriorityQueue(object):

    def __init__(self):
        self._list = []
        self.seniority = 0


    def insert(self, priority, val):
        '''inserts an item into the queue with the given priority and value'''

        self.seniority += 1
        self._list.append(Node(priority, val, self.seniority))

        child_pos = len(self._list) - 1

        while child_pos and (
                self._list[child_pos].priority > self._list[(child_pos - 1) // 2].priority):

            # swap parent and child
            self._switch(child_pos)
            child_pos = (child_pos - 1) // 2





        # new_item = Node(priority, val, self.front)
        # self.front = new_item

        # while new_item.next and new_item.priority >= new_item.next.priority:
        #     if new_item is self.front:
        #         self.front = new_item.next

        #     new_item.next , new_item.next.next = new_item.next.next, new_item


    def pop(self):
        try:
            self._list[0], self._list[-1] = self._list[-1], self._list[0]
            top = self._list.pop()

            parent_pos = 0
            children_pos = self._find_children(parent_pos)

            while children_pos != []:
                larger_child = None
                larger_child_index = None

                # If there are two children
                if len(children_pos) > 1:
                    if self._list[children_pos[0]].priority > self._list[
                            children_pos[1]].priority:
                        larger_child = self._list[children_pos[0]]
                        larger_child_index = children_pos[0]
                    elif self._list[children_pos[0]].priority < self._list[
                            children_pos[1]].priority:
                        larger_child = self._list[children_pos[1]]
                        larger_child_index = children_pos[1]

                    # if priorities are equal
                    else:
                        if self._list[children_pos[0]].seniority < self._list[
                                children_pos[1]].seniority:
                            larger_child = self._list[children_pos[0]]
                            larger_child_index = children_pos[0]

                        else:
                            larger_child = self._list[children_pos[1]]
                            larger_child_index = children_pos[1]

                # there is one child
                else:
                    larger_child = self._list[children_pos[0]]
                    larger_child_index = children_pos[0]

                # if the largest child's priority is greater than its parent, switch them
                if self._list[parent_pos].priority < larger_child.priority:
                    self._switch(larger_child_index)

                # if not, you're done
                else:
                    break
                parent_pos = larger_child_index
                children_pos = self._find_children(parent_pos)

            return top
        except IndexError:
            raise IndexError("The heap is empty")

    def peek():
        pass

    def _switch(self, child_index):
        """Helper, swaps the child at the given index with its parent"""
        parent_index = (child_index - 1) // 2

        self._list[parent_index], self._list[child_index] = (
            self._list[child_index], self._list[parent_index]
        )


    def _find_children(self, parent):
        '''Helper, returns a list of children for the given parent,
         an empty list if none
         '''

        children_indices = []

        if len(self._list) > 2*parent + 1:
            children_indices.append(2*parent+1)
        if len(self._list) > 2*parent + 2:
            children_indices.append(2*parent+2)

        return children_indices




class Node(object):
    def __init__(self, priority, val, seniority, next=None):
        self.priority = priority
        self.val = val
        self.next = None
        self.seniority = seniority