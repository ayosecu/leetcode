class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

tc = [
        0b00000010100101000001111010011100,
        0b11111111111111111111111111111101
    ]

sol = Solution()
for t in tc:
    print(format(sol.reverseBits(t), 'b'))