class Solution:
    def reverseWords(self, s: str) -> str:
        s.split()
        reverse_word = s[::-1]

        return ' '.join(reverse_word.split()[::-1])

        