class Solution:
    def combinationSum2(self, candidates, target):
        result = []

        candidates.sort()

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No need to continue if number is too large
                if candidates[i] > remaining:
                    break

                # Choose the number
                path.append(candidates[i])

                # i + 1 because each number can be used only once
                backtrack(i + 1, remaining - candidates[i], path)

                # Backtrack
                path.pop()

        backtrack(0, target, [])
        return result
