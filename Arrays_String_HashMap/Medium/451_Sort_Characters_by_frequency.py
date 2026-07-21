# STRING QUESTION 

# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.


class Solution:
    def frequencySort(self, s: str) -> str:

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        ans = ""

        for ch, count in sorted_chars: #Here ch is alphabet and count is its frequency
            ans += ch * count

        return ans
    
# Approach:
        # 1. Traverse the string and store the frequency of each character
        #    in a hash map (dictionary).
        # 2. Convert the dictionary into a list of (character, frequency)
        #    pairs and sort it in descending order of frequency.
        # 3. Build the final string by repeating each character according
        #    to its frequency and return the result.
        #
        # Time Complexity:
        # O(n + k log k)
        # - O(n) to count character frequencies.
        # - O(k log k) to sort the k distinct characters.
        # - O(n) to build the final string.
        # Overall: O(n + k log k)
        #
        # Space Complexity:
        # O(k)
        # - Dictionary stores frequencies of k distinct characters.
        # - Sorted list also stores k elements.