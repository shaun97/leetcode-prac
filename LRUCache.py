class DLNode:
    def __init__(self, key=0, value=0, prevNode=None, nextNode=None):
        self.key = key
        self.value = value
        self.prev = prevNode
        self.next = nextNode


class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.head = DLNode()
        self.tail = DLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_front(self, node):
        self.remove_node(node)

        # move to the front of the list
        # connect to the prev first node
        node.next = self.head.next
        self.head.next.prev = node

        node.prev = self.head
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        node = self.dict.get(key)
        if node:
            node = self.dict[key]
            self.move_to_front(node)
            return self.dict[key].value
        else:
            return -1

    def printLL(self):
        node = self.head.next
        LLstring = ""
        dictString = "{"

        while node.next:
            LLstring += f"[{node.key}: {node.value}] "
            node = node.next
        for key, item in self.dict.items():
            dictString += f"{key}: {item.value}, "
        dictString += "}"
        print(dictString)
        print(LLstring)

    def put(self, key: int, value: int) -> None:
        node = self.dict.get(key)
        if node:
            node = self.dict[key]
            self.move_to_front(node)
            node.value = value
        else:
            if self.capacity == 0:
                lastNodeKey = self.tail.prev.key
                self.remove_node(self.tail.prev)
                del self.dict[lastNodeKey]
                self.capacity += 1

            # python auto garbage collects
            # add new node in
            newNode = DLNode(value=value, key=key)

            newNode.next = self.head.next
            self.head.next.prev = newNode

            self.head.next = newNode
            newNode.prev = self.head

            self.dict[key] = newNode
            self.capacity -= 1

#         print(f"-----put {key} {value}-----")
#         self.printLL()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
