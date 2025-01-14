"""
Using Doubly Linked List + UnOrdered Dictionary
"""
class ListNode:
    def __init__(self, key: int, val: int, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capa = capacity
        self.dic = {}
        self.head = ListNode(-1, -1, None, None)
        self.tail = ListNode(-1, -1, None, None)
        self.head.next = self.tail

    def addNode(self, node: ListNode):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node

    def removeNode(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.dic:
            node_ptr = self.dic[key]
            self.removeNode(node_ptr)
            self.addNode(node_ptr)
            return node_ptr.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            # move node to head
            node_ptr = self.dic[key]
            self.removeNode(node_ptr)
            del self.dic[node_ptr.key]           

        # add to head
        tmp_node = ListNode(key, value)
        self.dic[key] = tmp_node
        self.addNode(tmp_node)
        
        if len(self.dic) > self.capa:
            tmp_node = self.tail.prev
            del self.dic[tmp_node.key]
            self.removeNode(self.tail.prev)


def run_tests():
    # Test cases
    test_cases = [
        {
            "operations": ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            "arguments": [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            "expected": [None, None, None, 1, None, -1, None, -1, 3, 4],
        },
        {
            "operations": ["LRUCache", "put", "get", "put", "get", "put", "get", "get"],
            "arguments": [[1], [2, 1], [2], [3, 2], [2], [4, 3], [2], [4]],
            "expected": [None, None, 1, None, -1, None, -1, 3],
        },
    ]

    for i, test_case in enumerate(test_cases, 1):
        operations = test_case["operations"]
        arguments = test_case["arguments"]
        expected = test_case["expected"]

        # Initialize the LRUCache
        lru = LRUCache(*arguments[0])

        results = []
        for op, args in zip(operations[1:], arguments[1:]):
            if op == "put":
                results.append(lru.put(*args))
            elif op == "get":
                results.append(lru.get(*args))

        # Include the initial "None" for initialization
        results = [None] + results

        print(f"Test case {i}: {'Passed' if results == expected else 'Failed'}, Result: {results}, Expected: {expected}")

# Run the tests
run_tests()