class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s) - 1):
         if roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
         else:
                total += roman_to_int[s[i]]

        total += roman_to_int[s[-1]]
        return total

s = input("Insert the characters: ")
sol = Solution()
print(sol.romanToInt(s))
        