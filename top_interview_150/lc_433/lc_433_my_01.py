from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        gene = { "A", "C", "G", "T" }
        dq = deque([(startGene, 0)])
        visited = set()
        visited.add(startGene)

        while dq:
            pop_gene, m_count = dq.popleft()
            if pop_gene == endGene:
                return m_count
            for i in range(len(pop_gene)):
                for c in gene:
                    temp_gene = pop_gene[:i] + c + pop_gene[i+1:]
                    if temp_gene in bank and temp_gene not in visited:
                        visited.add(temp_gene)
                        dq.append((temp_gene, m_count + 1))
        
        return -1

tc = [
        ["AACCGGTT", "AACCGGTA", ["AACCGGTA"]],
        ["AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"] ]
    ]

sol = Solution()
for t in tc:
    print(sol.minMutation(t[0], t[1], t[2]))
