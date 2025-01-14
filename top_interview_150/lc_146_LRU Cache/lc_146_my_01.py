"""
Using OrderedDict
"""
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capa = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capa:
            self.cache.popitem(last=False)


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