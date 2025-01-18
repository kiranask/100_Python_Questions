"""
SDET Interview | Coding Round | #Code6
Question: Write a Python function that compresses a given string. The function should replace sequences of the same character that appear consecutively in the string with the character followed by the number of times it appears consecutively. For example, the string "aabbbcccc" should be compressed to "a2b3c4". If a character does not repeat, it should remain as is. For example, the string "abc" should remain "abc".
#coding #python #pythonprogramming #testing #testinterview
"""

class Solution:
    def compress(self, given: str) -> str:
        n = len(given)
        if n == 0:
            return ""  # Handle empty input

        result = []
        count = 1  # Initialize count

        for i in range(1, n):
            if given[i] == given[i - 1]:
                count += 1
            else:
                result.append(given[i - 1])  # Append the character
                if count > 1:
                    result.append(str(count))  # Append the count if > 1
                count = 1  # Reset count

        # Append the last character and its count
        result.append(given[-1])
        if count > 1:
            result.append(str(count))

        return "".join(result)

# Example usage
solution = Solution()
compressed_string = solution.compress("aaabbcddddee")
print(compressed_string)  # Output: "a3b2cd4e2"
