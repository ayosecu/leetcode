import heapq

"""
    - Time Complexity: O(logn), n = The number of added numbers
    - Space Complexity: O(n), n = The number of added numbers
"""
class MedianFinder:

    def __init__(self):
        self.left_max_hq = []
        self.right_min_hq = []
      
    def addNum(self, num: int) -> None:
        if len(self.left_max_hq) == len(self.right_min_hq):
            heapq.heappush(self.right_min_hq, -heapq.heappushpop(self.left_max_hq, -num))
        else:
            heapq.heappush(self.left_max_hq, -heapq.heappushpop(self.right_min_hq, num))

    def findMedian(self) -> float:
        if len(self.left_max_hq) == len(self.right_min_hq):       
            return (-self.left_max_hq[0] + self.right_min_hq[0]) / 2
        else:
            return float(self.right_min_hq[0])


def run_tests():
    medianFinder = MedianFinder()

    test_cases = [
        # Format: (Numbers to insert, Expected median at each step)
        ([1, 2, 3], [1.0, 1.5, 2.0]),      # Odd number of elements
        ([5, 15, 1, 3], [5.0, 10.0, 5.0, 4.0]), # Even number of elements
        ([2, 4, 6, 8], [2.0, 3.0, 4.0, 5.0]),  # Evenly spaced values
        ([10, 20, 30, 40, 50], [10.0, 15.0, 20.0, 25.0, 30.0]), # Increasing numbers
        ([100], [100.0]),                   # Single element
        ([7, 3, 5, 2, 6, 8], [7.0, 5.0, 5.0, 4.0, 5.0, 5.5]), # Unordered insertion
    ]

    for i, (nums, expected_medians) in enumerate(test_cases, 1):
        medianFinder = MedianFinder()
        results = []
        for num in nums:
            medianFinder.addNum(num)
            results.append(medianFinder.findMedian())

        print(f"Test case {i}: {'Passed' if results == expected_medians else 'Failed'}")
        print(f"  Inserted: {nums}")
        print(f"  Results: {results}")
        print(f"  Expected: {expected_medians}\n")

# Run the tests
run_tests()