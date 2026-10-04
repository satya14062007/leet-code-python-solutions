class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, path):
            # Target reached
            if remaining == 0:
                result.append(path[:])
                return

            # Target exceeded
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                # Choose the number
                path.append(num)

                # Use same number again
                backtrack(i, remaining - num, path)

                # Backtrack
                path.pop()

        backtrack(0, target, [])
        return result
