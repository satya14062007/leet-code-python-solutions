class Solution:
    def findSubstring(self, s, words):
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        # Count how many times each word should appear
        required = {}
        for word in words:
            required[word] = required.get(word, 0) + 1

        result = []

        # Try each possible starting offset
        for offset in range(word_len):
            left = offset
            right = offset
            current = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word not in required:
                    # Invalid word: reset window
                    current = {}
                    count = 0
                    left = right
                    continue

                current[word] = current.get(word, 0) + 1
                count += 1

                # Too many copies of this word
                while current[word] > required[word]:
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

                # Found all required words
                if count == word_count:
                    result.append(left)

                    # Move window forward to find next possible answer
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

        return result
