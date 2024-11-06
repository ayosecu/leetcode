class MinStack(object):

    def __init__(self):
        self.min_st = []
        self.st = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.st.append(val)
        if not self.min_st:
            self.min_st.append(val)
        else:
            self.min_st.append(min(self.min_st[-1], val))
        
    def pop(self):
        """
        :rtype: None
        """
        if self.st:
            self.st.pop()
        if self.min_st:
            self.min_st.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.st[-1] if self.st else None
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.min_st[-1] if self.min_st else None


def run_tests():
    # Test case 1
    min_stack1 = MinStack()
    min_stack1.push(-2)
    min_stack1.push(0)
    min_stack1.push(-3)
    expected1_min = -3
    result1_min = min_stack1.getMin()
    print(f"Test 1 getMin {'passed' if result1_min == expected1_min else 'failed'}: Expected {expected1_min}, Got {result1_min}")
    
    min_stack1.pop()
    expected1_top = 0
    result1_top = min_stack1.top()
    print(f"Test 1 top {'passed' if result1_top == expected1_top else 'failed'}: Expected {expected1_top}, Got {result1_top}")
    
    expected1_min = -2
    result1_min = min_stack1.getMin()
    print(f"Test 1 getMin after pop {'passed' if result1_min == expected1_min else 'failed'}: Expected {expected1_min}, Got {result1_min}")

    # Test case 2:
    min_stack2 = MinStack()
    min_stack2.push(1)
    min_stack2.push(1)
    min_stack2.push(1)
    expected2_min = 1
    result2_min = min_stack2.getMin()
    print(f"Test 2 getMin {'passed' if result2_min == expected2_min else 'failed'}: Expected {expected2_min}, Got {result2_min}")
    
    min_stack2.pop()
    result2_min = min_stack2.getMin()
    print(f"Test 2 getMin after pop {'passed' if result2_min == expected2_min else 'failed'}: Expected {expected2_min}, Got {result2_min}")

    # Test case 3:
    min_stack3 = MinStack()
    min_stack3.push(2)
    min_stack3.push(0)
    min_stack3.push(3)
    min_stack3.push(0)
    expected3_min = 0
    result3_min = min_stack3.getMin()
    print(f"Test 3 getMin {'passed' if result3_min == expected3_min else 'failed'}: Expected {expected3_min}, Got {result3_min}")
    
    min_stack3.pop()
    result3_min = min_stack3.getMin()
    print(f"Test 3 getMin after first pop {'passed' if result3_min == expected3_min else 'failed'}: Expected {expected3_min}, Got {result3_min}")
    
    min_stack3.pop()
    expected3_min = 0
    result3_min = min_stack3.getMin()
    print(f"Test 3 getMin after second pop {'passed' if result3_min == expected3_min else 'failed'}: Expected {expected3_min}, Got {result3_min}")
    
    min_stack3.pop()
    expected3_min = 2
    result3_min = min_stack3.getMin()
    print(f"Test 3 getMin after third pop {'passed' if result3_min == expected3_min else 'failed'}: Expected {expected3_min}, Got {result3_min}")

# Run the tests
run_tests()