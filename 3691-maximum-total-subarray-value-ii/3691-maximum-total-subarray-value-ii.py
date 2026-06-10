from heapq import heappush, heappop


class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)
        levels = n.bit_length()

        maxs = [[0] * n for _ in range(levels)]

        mins = [[0] * n for _ in range(levels)]

        for i in range(n):
            maxs[0][i] = nums[i]
            mins[0][i] = nums[i]

        level = 1
        while (1 << level) <= n:
            half = 1 << (level - 1)
            for start in range(
                n - (1 << level) + 1
            ):
                maxs[level][start] = max(
                    maxs[level - 1][start],
                    maxs[level - 1][start + half]
                )
                mins[level][start] = min(
                    mins[level - 1][start],
                    mins[level - 1][start + half]
                )

            level += 1
        logs = [0] * (n + 1)

        for length in range(2, n + 1):
            logs[length] = logs[length // 2] + 1

        def value(left, right):
            length = right - left + 1
            power = logs[length]
            size = 1 << power
            maximum = max(
                maxs[power][left],
                maxs[power][right - size + 1]
            )

            minimum = min(
                mins[power][left],
                mins[power][right - size + 1]
            )

            return maximum - minimum

        heap = []
        for left in range(n):
            right = n - 1
            score = value(left, right)
            heappush(heap,(-score, left, right))
            

        total = 0
        for _ in range(k):
            score, left, right = heappop(heap)
            total += -score
            if right > left:
                nxt = right - 1
                score = value(left, nxt)
                heappush( heap, (-score, left, nxt))

        return total