class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        i = 0
        result = []
        while i < n:
            char = word[i]
            count = 1
            while (i + count < n) and (count < 9) and (char == word[i+count]):
                count += 1
            i += count
            result.append(f'{count}{char}')

        return "".join(result)     