from typing import List
from collections import deque

class Solution:

    """
        - Time Complexity: O(n), n = len(bank)
        - Space Complexity: O(n), n = len(bank)
        - Note
            - Nested for loop => constant, 8 * 4
    """
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)

        if endGene not in bank:
            return -1
        
        choices = { "A", "C", "G", "T" }
        dq = deque([(startGene, 0)])
        visited = set()

        while dq:
            pop_gene, m_count = dq.popleft()
            visited.add(pop_gene)
            if pop_gene == endGene:
                return m_count
            
            for i in range(8):
                for c in choices:
                    temp_gene = pop_gene[:i] + c + pop_gene[i+1:]
                    if temp_gene not in visited and temp_gene in bank:
                        dq.append((temp_gene, m_count + 1))
        
        return -1
    
tc = [
        ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
        ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2)
]

for i, (startGene, endGene, bank, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.minMutation(startGene, endGene, bank)
    print(f"TC {i} Passed!" if result == expected else f"TC {i} Failed!! - Expected: {expected}, Result: {result}")