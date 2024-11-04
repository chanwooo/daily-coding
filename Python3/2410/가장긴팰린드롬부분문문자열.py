class Solution:
    def longestPalindrome2(self, s: str) -> str:
        answer = ""

        for phase in range(2, len(s) + 1):
            for i in range(len(s)):
                word = s[i:i + phase]
                print(word)
                if isPalindrome(word) and len(word) == phase:
                    answer = word

        return answer

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        answer = ""
        for i in range(len(s) - 1):
            answer = max(answer, expand(i, i + 1), expand(i, i + 2), key=len)
        return answer


def isPalindrome(s):
    return s == s[::-1]


print("ans: ", Solution.longestPalindrome(Solution, "babad"))
print("ans: ", Solution.longestPalindrome(Solution, "abcdcba"))
