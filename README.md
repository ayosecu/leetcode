# leetcode
Coding exercise at leetcode

## ROI
| Topic | Difficulty to Learn | Return on Investment |
| ----- | ------------------- | -------------------- |
| Two Pointer | Easy | High |
| Sliding Window | Easy | High |
| BFS | Easy | High |
| DFS | Medium | High |
| Backtracking | High | High |
| Heap | Medium | Medium |
| Binary Search | Easy | Medium |
| Dynamic Programming | High | Medium |
| Divide and Conquer | Medium | Low |
| Trie | Medium | Low |
| Union Find | Medium | Low |
| Greedy | High | Low |

## 8 Patterns
### Linear Data Structure Patterns
1. *Two Pointers:*
  - Reduces time complexity to linear time \(O(n)\).
  - Two methods:
    - Same direction: used for scanning data in a single pass (e.g., fast and slow pointers to detect cycles or find middle elements).
    - Opposite directions: used for finding pairs (e.g., sum of two numbers in a sorted array).
2. *Sliding Window:*
  - Refines two pointers to manage a window of elements dynamically.
  - Expands or contracts the window to meet specific conditions (e.g., longest substring without repeating characters).
  - Often combined with hashmaps.
3. *Binary Search:*
  - Efficiently finds target in logarithmic time \(O(\log n)\).
  - Extends to lists with monotonic conditions, not just sorted numbers.
  - Example: finding the minimum in a rotated sorted array.

### Nonlinear Data Structure Patterns
4. *Breadth-First Search (BFS):*
  - Explores nodes level by level.
  - Uses a queue to keep track of visited nodes (ideal for level order traversal).
5. *Depth-First Search (DFS):*
  - Dives deep into one path before exploring others.
  - Often uses recursion and is memory efficient for exploring all paths.
  - Example: counting islands in a grid.
6. *Backtracking:*
  - Extension of DFS, explores all possible solutions.
  - Builds the solution dynamically by making decisions and backtracking on invalid paths.
  - Example: letter combinations of a phone number.

### Heaps (Priority Queue)
7. *Heaps:*
  - Used for questions related to top K, K smallest/largest.
  - *Min Heap:* smallest value at the root.
  - *Max Heap:* largest value at the root.
  - Max Heap is used to find K smallest values, and vice versa for K largest.

### Dynamic Programming (DP)
8. *Dynamic Programming:*
  - Optimizes solutions by breaking problems into overlapping subproblems.
    - Two approaches:
      - *Top-down:* recursive with memoization to store results.
      - *Bottom-up:* solves smaller subproblems iteratively using a table.
    - Too complex for this video but covered in-depth on their website.
 
## Backtracking
- [A general approach to backtracking](https://leetcode.com/problems/combination-sum/solutions/16502/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning/?envType=study-plan-v2&envId=top-interview-150)
